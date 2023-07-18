bl_info = {
    "name": "Duplicate Hotkeys Fix",
    "author": "abhiraaid",
    "version": (1, 0),
    "blender": (3, 6, 0),
    "category": "User",
}

import bpy

def set_custom_hotkeys():
    keymaps = bpy.context.window_manager.keyconfigs.default.keymaps
    node_editor_keymap = keymaps['Node Editor']

    for keymap_item in node_editor_keymap.keymap_items:
        if keymap_item.idname == 'node.duplicate_move':
            keymap_item.type = 'D'
            keymap_item.value = 'PRESS'
            keymap_item.ctrl = True
            keymap_item.shift = True
            keymap_item.repeat = True
        
        elif keymap_item.idname == 'node.duplicate_move_keep_inputs':
            keymap_item.type = 'D'
            keymap_item.value = 'PRESS'
            keymap_item.ctrl = True
            keymap_item.shift = False
            keymap_item.repeat = True

class WM_OT_SetCustomHotkeysOperator(bpy.types.Operator):
    bl_idname = "wm.set_custom_hotkeys_operator"
    bl_label = "Set Custom Hotkeys Operator"

    def execute(self, context):
        set_custom_hotkeys()
        return {'FINISHED'}

def register():
    bpy.utils.register_class(WM_OT_SetCustomHotkeysOperator)

    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Window', space_type='EMPTY')
    kmi = km.keymap_items.new("wm.set_custom_hotkeys_operator", type='SPACE', value='PRESS', alt=True, oskey=True)

    print("Duplicate Hotkeys Fix add-on registered.")

def unregister():
    bpy.utils.unregister_class(WM_OT_SetCustomHotkeysOperator)

    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.get('Window', None)
    if km:
        wm.keyconfigs.addon.keymaps.remove(km)

    print("Duplicate Hotkeys Fix add-on unregistered.")

if __name__ == "__main__":
    register()

