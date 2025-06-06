import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = app.activeProduct

        rootComp = design.rootComponent
        sketches = rootComp.sketches
        xyPlane = rootComp.xYConstructionPlane

        # Draw a center rectangle 85mm x 85mm
        sketch = sketches.add(xyPlane)
        sketchRect = sketch.sketchCurves.sketchLines.addCenterPointRectangle(
            adsk.core.Point3D.create(0, 0, 0),
            adsk.core.Point3D.create(42.5, 42.5, 0)
        )

        # Extrude the profile to 20mm height
        prof = sketch.profiles.item(0)
        extrudes = rootComp.features.extrudeFeatures
        extInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        distance = adsk.core.ValueInput.createByReal(20.0)
        extInput.setDistanceExtent(False, distance)
        baseExtrude = extrudes.add(extInput)

        # Shell the block to create 2mm walls (remove top face)
        faces = baseExtrude.endFaces
        topFace = None
        for face in faces:
            if face.pointOnFace.z > 10:  # top face is highest
                topFace = face
                break

        if topFace is None:
            ui.messageBox('Top face not found. Shell operation skipped.')
            return

        shellFeats = rootComp.features.shellFeatures
        facesToShell = adsk.core.ObjectCollection.create()
        facesToShell.add(topFace)
        shellInput = shellFeats.createInput(facesToShell)
        shellInput.insideThickness = adsk.core.ValueInput.createByReal(2.0)
        shellFeats.add(shellInput)

        ui.messageBox('HELEN base with 2mm walls created!')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
