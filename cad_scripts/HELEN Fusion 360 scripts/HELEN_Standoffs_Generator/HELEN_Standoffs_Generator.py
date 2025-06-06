import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = app.activeProduct
        rootComp = design.rootComponent

        # Get HELEN base body
        baseBody = None
        for body in rootComp.bRepBodies:
            if body.name == 'HELEN_Base':
                baseBody = body
                break
        if not baseBody:
            ui.messageBox('HELEN_Base not found.')
            return

        # Create sketch on top face of the base floor (assumed XY plane at Z = 0)
        sketch = rootComp.sketches.add(rootComp.xYConstructionPlane)
        circles = sketch.sketchCurves.sketchCircles

        # Position 4 standoffs at corners of a 60mm square
        r = 1.5  # radius = 1.5 mm → 3 mm diameter
        h = 10   # height in mm

        positions = [
            adsk.core.Point3D.create(-30, -30, 0),
            adsk.core.Point3D.create(-30,  30, 0),
            adsk.core.Point3D.create( 30, -30, 0),
            adsk.core.Point3D.create( 30,  30, 0)
        ]

        for pt in positions:
            circles.addByCenterRadius(pt, r)

        # Extrude each standoff upward
        profs = sketch.profiles
        extrudes = rootComp.features.extrudeFeatures
        for i in range(profs.count):
            extInput = extrudes.createInput(profs.item(i), adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
            extInput.setDistanceExtent(False, adsk.core.ValueInput.createByReal(h))
            extrudes.add(extInput)

        ui.messageBox('4 internal standoffs created!')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
