import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = app.activeProduct
        rootComp = design.rootComponent

        # Get HELEN_Base body
        baseBody = None
        for body in rootComp.bRepBodies:
            if body.name == 'HELEN_Base':
                baseBody = body
                break
        if not baseBody:
            ui.messageBox('HELEN_Base not found.')
            return

        # Create a construction plane offset from front face (Y+)
        offsetPlaneInput = rootComp.constructionPlanes.createInput()
        offsetPlaneInput.setByOffset(rootComp.xYConstructionPlane, adsk.core.ValueInput.createByReal(42.5))
        plane = rootComp.constructionPlanes.add(offsetPlaneInput)

        # Create sketch on the offset plane
        sketch = rootComp.sketches.add(plane)
        circles = sketch.sketchCurves.sketchCircles
        # Place vent hole center at (0, 0) → aligns to center of wall
        circles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 10), 2.0)

        # Cut inward into body
        prof = sketch.profiles.item(0)
        extrudes = rootComp.features.extrudeFeatures
        extInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.CutFeatureOperation)
        depth = adsk.core.ValueInput.createByReal(-5.0)  # negative = inward
        extInput.setDistanceExtent(False, depth)
        extInput.participantBodies = [baseBody]
        extrudes.add(extInput)

        ui.messageBox('Thermal vent created from offset plane!')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
