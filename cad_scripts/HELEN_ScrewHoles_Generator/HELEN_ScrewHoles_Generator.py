import adsk.core, adsk.fusion, adsk.cam, traceback
import math

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = app.activeProduct
        rootComp = design.rootComponent

        # Define screw hole parameters
        hole_radius = 1.3  # ~2.6 mm diameter for M2.5
        hole_depth = 10.0

        # Loop through all bodies to find vertical cylinders (standoffs)
        extrudes = rootComp.features.extrudeFeatures
        standoffs = []
        for body in rootComp.bRepBodies:
            if body.name.startswith('Body'):  # standoffs likely unnamed cylinders
                # Check if it’s roughly cylindrical and vertical
                bb = body.boundingBox
                height = bb.maxPoint.z - bb.minPoint.z
                radius = (bb.maxPoint.x - bb.minPoint.x) / 2
                if abs(height - 10.0) < 0.5 and abs(radius - 1.5) < 0.5:
                    standoffs.append(body)

        if len(standoffs) != 4:
            ui.messageBox(f'Expected 4 standoffs, found {len(standoffs)}. Make sure they were created first.')
            return

        for standoff in standoffs:
            # Create a sketch on top of each standoff
            topFace = None
            for face in standoff.faces:
                if face.geometry.surfaceType == adsk.core.SurfaceTypes.PlaneSurfaceType:
                    normal = face.evaluator.getNormalAtPoint(face.pointOnFace)[1]
                    if abs(normal.z - 1.0) < 0.01:
                        topFace = face
                        break

            if not topFace:
                continue

            sketch = rootComp.sketches.add(topFace)
            circles = sketch.sketchCurves.sketchCircles
            circles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), hole_radius)

            # Cut the hole into the standoff
            profile = sketch.profiles.item(0)
            extInput = extrudes.createInput(profile, adsk.fusion.FeatureOperations.CutFeatureOperation)
            depth = adsk.core.ValueInput.createByReal(-hole_depth)
            extInput.setDistanceExtent(False, depth)
            extInput.participantBodies = [standoff]
            extrudes.add(extInput)

        ui.messageBox('M2.5 screw holes added to all standoffs!')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
