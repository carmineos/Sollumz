import traceback
from genericpath import exists
import bpy
from Sollumz.sollumz_helper import SOLLUMZ_OT_base
from Sollumz.sollumz_properties import BoundType, PolygonType, SOLLUMZ_UI_NAMES
from Sollumz.meshhelper import *
from Sollumz.tools.boundhelper import *
from Sollumz.ybn.collision_materials import create_collision_material_from_index
from Sollumz.ybn.properties import BoundFlags, load_flag_presets, flag_presets, get_flag_presets_path
from Sollumz.resources.flag_preset import FlagPreset


def handle_load_flag_presets(self):
    try:
        load_flag_presets()
    except FileNotFoundError:
        self.report({'ERROR'}, traceback.format_exc())


class SOLLUMZ_OT_create_bound_composite(SOLLUMZ_OT_base, bpy.types.Operator):
    """Create a sollumz bound composite"""
    bl_idname = "sollumz.createboundcomposite"
    bl_label = f"Create {SOLLUMZ_UI_NAMES[BoundType.COMPOSITE]}"
    bl_action = f"Create a {SOLLUMZ_UI_NAMES[BoundType.COMPOSITE]}"

    def run(self, context):
        selected = context.selected_objects
        if len(selected) < 1:
            try:
                create_bound()
                return self.success()
            except:
                return self.fail(traceback.format_exc())
        else:
            try:
                convert_selected_to_bound(
                    selected, context.scene.use_mesh_name, context.scene.create_seperate_objects)
                return self.success()
            except:
                return self.fail(traceback.format_exc())


class SOLLUMZ_OT_create_geometry_bound(SOLLUMZ_OT_base, bpy.types.Operator):
    """Create a sollumz geometry bound"""
    bl_idname = "sollumz.creategeometrybound"
    bl_label = f"Create {SOLLUMZ_UI_NAMES[BoundType.GEOMETRY]}"
    bl_action = f"Create a {SOLLUMZ_UI_NAMES[BoundType.GEOMETRY]}"

    def run(self, context):
        try:
            gobj = create_bound(BoundType.GEOMETRY)
            context.view_layer.objects.active = bpy.data.objects[gobj.name]
            return self.success()
        except:
            return self.fail(traceback.format_exc())


class SOLLUMZ_OT_create_geometrybvh_bound(SOLLUMZ_OT_base, bpy.types.Operator):
    """Create a sollumz geometry bound bvh"""
    bl_idname = "sollumz.creategeometryboundbvh"
    bl_label = f"Create {SOLLUMZ_UI_NAMES[BoundType.GEOMETRYBVH]}"
    bl_action = f"Create a {SOLLUMZ_UI_NAMES[BoundType.GEOMETRYBVH]}"

    def run(self, context):
        try:
            gobj = create_bound(BoundType.GEOMETRYBVH)
            context.view_layer.objects.active = bpy.data.objects[gobj.name]
            return self.success()
        except:
            return self.fail(traceback.format_exc())


class SOLLUMZ_OT_create_box_bound(SOLLUMZ_OT_base, bpy.types.Operator):
    """Create a sollumz box bound"""
    bl_idname = "sollumz.createboxbound"
    bl_label = f"Create {SOLLUMZ_UI_NAMES[BoundType.BOX]}"
    bl_action = f"Create a {SOLLUMZ_UI_NAMES[BoundType.BOX]}"

    def run(self, context):
        try:
            gobj = create_bound(BoundType.BOX)
            context.view_layer.objects.active = bpy.data.objects[gobj.name]
            return self.success()
        except:
            return self.fail(traceback.format_exc())


class SOLLUMZ_OT_create_sphere_bound(SOLLUMZ_OT_base, bpy.types.Operator):
    """Create a sollumz sphere bound"""
    bl_idname = "sollumz.createspherebound"
    bl_label = f"Create {SOLLUMZ_UI_NAMES[BoundType.SPHERE]}"
    bl_action = f"Create a {SOLLUMZ_UI_NAMES[BoundType.SPHERE]}"

    def run(self, context):
        try:
            gobj = create_bound(BoundType.SPHERE)
            context.view_layer.objects.active = bpy.data.objects[gobj.name]
            return self.success()
        except:
            return self.fail(traceback.format_exc())


class SOLLUMZ_OT_create_capsule_bound(SOLLUMZ_OT_base, bpy.types.Operator):
    """Create a sollumz capsule bound"""
    bl_idname = "sollumz.createcapsulebound"
    bl_label = f"Create {SOLLUMZ_UI_NAMES[BoundType.CAPSULE]}"
    bl_action = f"Create a {SOLLUMZ_UI_NAMES[BoundType.CAPSULE]}"

    def run(self, context):
        try:
            gobj = create_bound(BoundType.CAPSULE)
            context.view_layer.objects.active = bpy.data.objects[gobj.name]
            return self.success()
        except:
            return self.fail(traceback.format_exc())


class SOLLUMZ_OT_create_cylinder_bound(SOLLUMZ_OT_base, bpy.types.Operator):
    """Create a sollumz cylinder bound"""
    bl_idname = "sollumz.createcylinderbound"
    bl_label = f"Create {SOLLUMZ_UI_NAMES[BoundType.CYLINDER]}"
    bl_action = f"Create a {SOLLUMZ_UI_NAMES[BoundType.CYLINDER]}"

    def run(self, context):
        try:
            gobj = create_bound(BoundType.CYLINDER)
            context.view_layer.objects.active = bpy.data.objects[gobj.name]
            return self.success()
        except:
            return self.fail(traceback.format_exc())


class SOLLUMZ_OT_create_disc_bound(SOLLUMZ_OT_base, bpy.types.Operator):
    """Create a sollumz disc bound"""
    bl_idname = "sollumz.creatediscbound"
    bl_label = f"Create {SOLLUMZ_UI_NAMES[BoundType.DISC]}"
    bl_action = f"Create a {SOLLUMZ_UI_NAMES[BoundType.DISC]}"

    def run(self, context):
        try:
            gobj = create_bound(BoundType.DISC)
            context.view_layer.objects.active = bpy.data.objects[gobj.name]
            return self.success()
        except:
            return self.fail(traceback.format_exc())


class SOLLUMZ_OT_create_cloth_bound(SOLLUMZ_OT_base, bpy.types.Operator):
    """Create a sollumz cloth bound"""
    bl_idname = "sollumz.createclothbound"
    bl_label = f"Create {SOLLUMZ_UI_NAMES[BoundType.CLOTH]}"
    bl_action = f"Create a {SOLLUMZ_UI_NAMES[BoundType.CLOTH]}"

    def run(self, context):
        try:
            gobj = create_bound(BoundType.CLOTH)
            context.view_layer.objects.active = bpy.data.objects[gobj.name]
            return self.success()
        except:
            return self.fail(traceback.format_exc())


class SOLLUMZ_OT_create_polygon_bound(SOLLUMZ_OT_base, bpy.types.Operator):
    """Create a sollumz polygon bound"""
    bl_idname = "sollumz.createpolygonbound"
    bl_label = "Create Polygon Bound"
    bl_action = f"{bl_label}"

    def create_poly(self, aobj, type):
        if not (aobj and (aobj.sollum_type == BoundType.GEOMETRY or aobj.sollum_type == BoundType.GEOMETRYBVH)):
            raise Exception(
                f"Please select a {SOLLUMZ_UI_NAMES[BoundType.GEOMETRYBVH]} or {SOLLUMZ_UI_NAMES[BoundType.GEOMETRY]} to add a {SOLLUMZ_UI_NAMES[type]} to.")

        pobj = create_bound(type, True)

        if type == PolygonType.BOX:
            create_box(pobj.data)
        elif type == PolygonType.SPHERE:
            create_sphere(pobj.data)
        elif type == PolygonType.CAPSULE:
            create_capsule(pobj)
        elif type == PolygonType.CYLINDER:
            create_cylinder(pobj.data)

        pobj.parent = aobj
        # bpy.context.view_layer.objects.active = bpy.data.objects[cobj.name] if you enable this you wont be able to stay selecting the composite obj...

    def create_poly_from_verts(self, aobj, type, parent):
        if not parent:
            raise Exception("Must specify a parent object!")
        elif parent.sollum_type != BoundType.GEOMETRYBVH and parent.sollum_type != BoundType.GEOMETRY:
            raise Exception(
                f'Parent must be a {SOLLUMZ_UI_NAMES[BoundType.GEOMETRYBVH]} or {SOLLUMZ_UI_NAMES[BoundType.GEOMETRY]}!')

        # We need to switch from Edit mode to Object mode so the vertex selection gets updated (disgusting!)
        bpy.ops.object.mode_set(mode='OBJECT')
        selected_verts = [Vector((v.co.x, v.co.y, v.co.z))
                          for v in aobj.data.vertices if v.select]
        bpy.ops.object.mode_set(mode='EDIT')

        if len(selected_verts) < 1:
            raise Exception('No vertices selected.')

        pobj = create_bound(type, True)

        np_array = np.array(selected_verts)
        bbmin_local = Vector(np_array.min(axis=0))
        bbmax_local = Vector(np_array.max(axis=0))
        bbmin = aobj.matrix_world @ bbmin_local
        bbmax = aobj.matrix_world @ bbmax_local

        radius = ((aobj.matrix_local @ bbmax).x -
                  (aobj.matrix_local @ bbmin).x) / 2
        height = get_distance_of_vectors(bbmin, bbmax)
        center = (bbmin + bbmax) / 2
        pobj.location = center

        if type == PolygonType.BOX:
            scale = aobj.matrix_world.to_scale()
            min = (bbmin_local) * scale
            max = (bbmax_local) * scale
            center = (min + max) / 2
            create_box_from_extents(pobj.data, min - center, max - center)
            # pobj.location = Vector()
        elif type == PolygonType.SPHERE:
            create_sphere(pobj.data, height / 2)
        elif type == PolygonType.CAPSULE or type == PolygonType.CYLINDER:
            if type == PolygonType.CAPSULE:
                # height = height - (radius * 2)
                create_capsule(pobj, radius, height)
            elif type == PolygonType.CYLINDER:
                create_cylinder(pobj.data, radius, height, False)

        pobj.rotation_euler = aobj.rotation_euler

        pobj.parent = parent

    def run(self, context):
        aobj = context.active_object
        type = context.scene.poly_bound_type
        parent = context.scene.poly_parent

        if aobj.mode == "EDIT":
            try:
                self.create_poly_from_verts(aobj, type, parent)
                return self.success(
                    f"of type: {SOLLUMZ_UI_NAMES[type]}")
            except:
                return self.fail(traceback.format_exc())
        else:
            try:
                self.create_poly(aobj, type)
                self.success(
                    f"of type: {SOLLUMZ_UI_NAMES[type]}")
            except:
                return self.fail(traceback.format_exc())


class SOLLUMZ_OT_center_composite(SOLLUMZ_OT_base, bpy.types.Operator):
    """Center a bound composite with the rest of it's geometry. Note: Has no effect on export"""
    bl_idname = "sollumz.centercomposite"
    bl_label = "Center Composite"
    bl_action = f"{bl_label}"

    def run(self, context):
        aobj = context.active_object
        if not aobj:
            return self.fail(f"No {SOLLUMZ_UI_NAMES[BoundType.COMPOSITE]} selected.")
        if aobj.sollum_type != BoundType.COMPOSITE:
            return self.fail(f"{aobj.name} must be a {SOLLUMZ_UI_NAMES[BoundType.COMPOSITE]}!")
        if context.mode != 'OBJECT':
            return self.fail(f"{self.bl_idname} can only be ran in Object mode.")

        try:
            center = get_bound_center(aobj)
            aobj.location = center
            for obj in aobj.children:
                obj.delta_location = -center
            return self.success()
        except:
            return self.fail(traceback.format_exc())


class SOLLUMZ_OT_create_collision_material(SOLLUMZ_OT_base, bpy.types.Operator):
    """Create a sollumz collision material"""
    bl_idname = "sollumz.createcollisionmaterial"
    bl_label = "Create Collision Material"
    bl_action = f"{bl_label}"

    def run(self, context):

        selected = context.selected_objects
        if len(selected) < 1:
            return self.fail("No objects selected")

        for obj in selected:
            try:
                mat = create_collision_material_from_index(
                    context.scene.collision_material_index)
                obj.data.materials.append(mat)
                self.messages.append(
                    f"Succesfully added {mat.name} material to {obj.name}")
            except:
                self.messages.append(f"Failure to add material to {obj.name}")

        return self.success(None, False)


class SOLLUMZ_OT_delete_flag_preset(SOLLUMZ_OT_base, bpy.types.Operator):
    """Delete a flag preset"""
    bl_idname = "sollumz.delete_flag_preset"
    bl_label = "Delete Flag Preset"
    bl_action = f"{bl_label}"

    preset_blacklist = ['Default']

    def run(self, context):
        index = context.scene.flag_preset_index
        handle_load_flag_presets(self)

        try:
            preset = flag_presets.presets[index]
            if preset.name in self.preset_blacklist:
                return self.fail(f"Cannot delete a default preset!")

            filepath = get_flag_presets_path()
            flag_presets.presets.remove(preset)

            try:
                flag_presets.write_xml(filepath)
                handle_load_flag_presets(self)

                return self.success()
            except:
                return self.fail(f"Cannot delete a default preset!")

        except IndexError:
            return self.fail(f"Flag preset does not exist! Ensure the preset file is present in the '{filepath}' directory.")


class SOLLUMZ_OT_save_flag_preset(SOLLUMZ_OT_base, bpy.types.Operator):
    """Save a flag preset"""
    bl_idname = "sollumz.save_flag_preset"
    bl_label = "Save Flag Preset"
    bl_action = f"{bl_label}"

    def run(self, context):
        obj = context.active_object
        handle_load_flag_presets(self)

        if not obj:
            return self.fail("No object selected!")

        if obj.sollum_type and not (obj.sollum_type == BoundType.GEOMETRY or obj.sollum_type == BoundType.GEOMETRYBVH):
            return self.fail(f"Selected object must be either a {SOLLUMZ_UI_NAMES[BoundType.GEOMETRY]} or {SOLLUMZ_UI_NAMES[BoundType.GEOMETRYBVH]}!")

        name = context.scene.new_flag_preset_name
        if len(name) < 1:
            return self.fail(f'Please specify a name for the new flag preset.')

        flag_preset = FlagPreset()
        flag_preset.name = name

        for prop in dir(obj.composite_flags1):
            value = getattr(obj.composite_flags1, prop)
            if value == True:
                flag_preset.flags1.append(prop)

        for prop in dir(obj.composite_flags2):
            value = getattr(obj.composite_flags2, prop)
            if value == True:
                flag_preset.flags2.append(prop)

        filepath = get_flag_presets_path()

        for preset in flag_presets.presets:
            if preset.name == name:
                return self.fail(f'A preset with that name already exists! If you wish to overwrite this preset, delete the original.')

        try:
            flag_presets.presets.append(flag_preset)
            flag_presets.write_xml(filepath)
            handle_load_flag_presets(self)

            return self.success()
        except:
            return self.fail(traceback.format_exc())


class SOLLUMZ_OT_load_flag_preset(SOLLUMZ_OT_base, bpy.types.Operator):
    """Load a flag preset to the selected Geometry bounds"""
    bl_idname = "sollumz.load_flag_preset"
    bl_label = "Apply Flags Preset"
    bl_context = 'object'
    bl_options = {'REGISTER', 'UNDO'}
    bl_action = f"{bl_label}"

    def run(self, context):
        index = context.scene.flag_preset_index
        selected = context.selected_objects
        if len(selected) < 1:
            return self.fail("No objects selected!")

        handle_load_flag_presets(self)

        for obj in selected:
            if obj.sollum_type and not (obj.sollum_type == BoundType.GEOMETRY or obj.sollum_type == BoundType.GEOMETRYBVH):
                self.messages.append(
                    f"Object: {obj.name} will be skipped because it is not a {SOLLUMZ_UI_NAMES[BoundType.GEOMETRY]} or {SOLLUMZ_UI_NAMES[BoundType.GEOMETRYBVH]}!")

            try:
                preset = flag_presets.presets[index]

                for flag_name in BoundFlags.__annotations__.keys():
                    if flag_name in preset.flags1:
                        obj.composite_flags1[flag_name] = True
                    else:
                        obj.composite_flags1[flag_name] = False

                    if flag_name in preset.flags2:
                        obj.composite_flags2[flag_name] = True
                    else:
                        obj.composite_flags2[flag_name] = False

                # Hacky way to force the UI to redraw. For some reason setting custom properties will not cause the object properties panel to redraw, so we have to do this.
                obj.location = obj.location
                self.messages.append(
                    f"Succesfully Added Flag Preset To {obj.name}")
            except IndexError:
                filepath = get_flag_presets_path()
                self.messages.append(
                    f"Flag preset does not exist! Ensure the preset file is present in the '{filepath}' directory.")

        return self.success(None, False)


class SOLLUMZ_OT_clear_col_flags(SOLLUMZ_OT_base, bpy.types.Operator):
    """Load commonly used collision flags"""
    bl_idname = "sollumz.clear_col_flags"
    bl_label = "Clear Collision Flags"
    bl_action = f"{bl_label}"

    def run(self, context):

        aobj = context.active_object
        if(aobj == None):
            return self.fail(f"Please select a object to {self.bl_action}")

        if SOLLUMZ_OT_base.is_sollum_type(aobj, BoundType):
            for flag_name in BoundFlags.__annotations__.keys():
                aobj.composite_flags1[flag_name] = False
                aobj.composite_flags2[flag_name] = False

        return self.success()
