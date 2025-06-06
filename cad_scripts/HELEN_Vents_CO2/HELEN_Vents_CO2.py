import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = app.activeProduct
        rootComp = design.rootComponent

        # Find the HELEN base body
        baseBody = None
        for body in rootComp.bRepBodies:
            if body.name == 'HELEN_Base':
                baseBody = body
                break
        if not baseBody:
            ui.messageBox('HELEN_Base not found.')
            return

        # Create a construction plane offset from XZ plane (right wall)
        planeInput = rootComp.constructionPlanes.createInput()
        planeInput.setByOffset(rootComp.yZConstructionPlane, adsk.core.ValueInput.createByReal(42.5))
        sidePlane = rootComp.constructionPlanes.add(planeInput)

        # Create sketch on side wall offset plane
        sketch = rootComp.sketches.add(sidePlane)
        circles = sketch.sketchCurves.sketchCircles
        # Place hole at (Y=0, Z=5)
        circles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 5), 2.5)  # radius = 2.5 mm

        # Cut into the body
        profile = sketch.profiles.item(0)
        extrudes = rootComp.features.extrudeFeatures
        extInput = extrudes.createInput(profile, adsk.fusion.FeatureOperations.CutFeatureOperation)
        depth = adsk.core.ValueInput.createByReal(-5.0)
        extInput.setDistanceExtent(False, depth)
        extInput.participantBodies = [baseBody]
        extrudes.add(extInput)

        ui.messageBox('CO₂ vent created on side wall!')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
