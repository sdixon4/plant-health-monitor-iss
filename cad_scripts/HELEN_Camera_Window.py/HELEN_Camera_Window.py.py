import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = app.activeProduct
        rootComp = design.rootComponent

        # Find the base body
        baseBody = None
        for body in rootComp.bRepBodies:
            if body.name == 'HELEN_Base':
                baseBody = body
                break
        if not baseBody:
            ui.messageBox('HELEN_Base not found.')
            return

        # Create construction plane offset to front wall (Y+)
        planeInput = rootComp.constructionPlanes.createInput()
        planeInput.setByOffset(rootComp.xYConstructionPlane, adsk.core.ValueInput.createByReal(42.5))
        camPlane = rootComp.constructionPlanes.add(planeInput)

        # Create sketch on front wall
        sketch = rootComp.sketches.add(camPlane)
        rect = sketch.sketchCurves.sketchLines.addCenterPointRectangle(
            adsk.core.Point3D.create(0, 0, 15),  # center at Z = 15 mm
            adsk.core.Point3D.create(5, 3, 15)   # creates 10 × 6 mm rectangle
        )

        # Cut the camera hole inward
        prof = sketch.profiles.item(0)
        extrudes = rootComp.features.extrudeFeatures
        extInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.CutFeatureOperation)
        extInput.setDistanceExtent(False, adsk.core.ValueInput.createByReal(-5.0))
        extInput.participantBodies = [baseBody]
        extrudes.add(extInput)

        ui.messageBox('Camera window cutout added to front wall!')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
