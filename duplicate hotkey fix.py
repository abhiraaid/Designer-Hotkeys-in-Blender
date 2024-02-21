bl_info = {
    "name": "Duplicate Hotkeys Fix",
    "author": "abhiraaid",
    "version": (1, 1),
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

def register():
    set_custom_hotkeys()
    print("Duplicate Hotkeys Fix add-on registered.")

def unregister():
    print("Duplicate Hotkeys Fix add-on unregistered.")

if __name__ == "__main__":
    register()
