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

        # Create lid sketch on same XY plane
        sketch = sketches.add(xyPlane)
        sketchRect = sketch.sketchCurves.sketchLines.addCenterPointRectangle(
            adsk.core.Point3D.create(0, 0, 0),
            adsk.core.Point3D.create(42.5, 42.5, 0)
        )

        # Extrude to create 2mm-thick lid
        prof = sketch.profiles.item(0)
        extrudes = rootComp.features.extrudeFeatures
        extInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        distance = adsk.core.ValueInput.createByReal(2.0)
        extInput.setDistanceExtent(False, distance)

        # Position it 20mm up to sit on top of base
        extInput.setOneSideExtent(
            adsk.fusion.DistanceExtentDefinition.create(
                adsk.core.ValueInput.createByReal(20.0)
            ),
            adsk.fusion.ExtentDirections.PositiveExtentDirection
        )

        extrudes.add(extInput)

        ui.messageBox('Removable HELEN lid created!')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
