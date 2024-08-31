from ursina import *
import threading
import time
from ursina.prefabs.first_person_controller import FirstPersonController

# https://minecraft.fandom.com/wiki/List_of_block_textures


Data = [[[None for ___ in range(-50, 50, 1)] for _ in range(-50, 50, 1)] for __ in range(-50, 50, 1)]


class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture=load_texture("assets/skybox.PNG"),
            scale=150,
            double_sided=True
        )


class UnityTab:
    player = None
    def __init__(self):
        self.mainloop()

    def mainloop(self):
        global player
        global app

        print("###########")
        print("urs loaded")
        app = Ursina(size=(1000, 600))

        tab = Inventory()
        Inventory.add(tab, "GrassBlock")
        Inventory.add(tab, "DirtBlock")
        Inventory.add(tab, "Button")
        Inventory.add(tab, "IronBlock")
        Inventory.add(tab, "LampBlock")
        Inventory.add(tab, "Redstone")
        Inventory.add(tab, "RedstoneBlock")
        Inventory.add(tab, "Redstonetorch")
        Inventory.add(tab, "Repeater")
        Inventory.add(tab, "StoneBlock")
        Inventory.add(tab, "Switch")

        for z in range(-30, 30, 1):
            for x in range(-30, 30, 1):
                Data[int(x)][0][int(z)] = GrassBlock(position=(x, 0, z))

        UnityTab.player = FirstPersonController()

        sky = Sky()
        print("untity loaded")
        app.run()


class block(Button):
    def getProperties(self):
        print("block type")


class Inventory:
    DEFAULT = 1
    length = 0
    Index = []
    selected = DEFAULT

    def add(self, item):
        Inventory.Index.append(item)
        Inventory.length += 1
        #print("add item")

    def remove(self, item):
        try:
            Inventory.Index.remove(item)
            Inventory.length -= 1
            #print("remove item")
        except:
            print("can't remove")

    def getlength(self):
        return Inventory.length


class ButtonBlock(block):
    BUTTON_OFF = False
    BUTTON_ON = True

    interaction = BUTTON_OFF

    def __init__(self, position=(5, 2, 5)):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block/buttonoff',
            texture=load_texture('assets/block/buttontexture.png'),
            origin_y=0.5,
            color=color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.lime,
        )
        self.rotation_x = 180

    def input(self, key):
        if self.hovered:
            if key == 'z':
                self.interaction = not self.interaction
                if self.interaction:
                    super().__init__(
                        parent=scene,
                        position=self.position,
                        model="assets/block/buttonon",
                        texture=load_texture("assets/block/buttontexture.png"),
                        origin_y=0.5,
                        color=color.color(0, 0, random.uniform(.9, 1.0)),
                        highlight_color=color.lime,
                    )
                    self.rotation_x = 180
                else:
                    super().__init__(
                        parent=scene,
                        position=self.position,
                        model="assets/block/buttonoff",
                        texture=load_texture("assets/block/buttontexture.png"),
                        origin_y=0.5,
                        color=color.color(0, 0, random.uniform(.9, 1.0)),
                        highlight_color=color.lime,
                    )
                    self.rotation_x = 180

            if key == 'left mouse down':
                temp = Vec3(mouse.normal.x, -mouse.normal.y, -mouse.normal.z)
                position = self.position + temp
                setdisplay(position.x, position.y, position.z)

            if key == 'right mouse down':
                global Data
                position = self.position
                Data[int(position.x)][int(position.y)][int(position.z)] = None
                destroy(self)

    def getData(self):
        return "ButtonBlcck"

    def getProperties(self):
        if self.interaction == self.BUTTON_OFF:
            return "BUTTON_OFF"
        elif self.interaction == self.BUTTON_ON:
            return "BUTTON_ON"
        else:
            return "ERROR"

    def setProperties(self, STAT):
        if STAT == "BUTTON_OFF":
            self.interaction = self.BUTTON_OFF
            block.__init__(
                self,
                parent=scene,
                position=self.position,
                model="assets/block/buttonoff",
                texture=load_texture("assets/block/buttontexture.png"),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
        elif STAT == "BUTTON_ON":
            self.interaction = self.BUTTON_ON
            block.__init__(
                self,
                parent=scene,
                position=self.position,
                model="assets/block/buttonon",
                texture=load_texture("assets/block/buttontexture.png"),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
        else:
            print("CLASS = Button :: WRONG STAT")


class DirtBlock(block):
    interaction = None
    electricity = False

    def __init__(self, position=(5, 2, 5)):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block/dirt',
            texture=load_texture('assets/block/dirttexture.png'),
            origin_y=0.5,
            color=color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.lime,
        )
        self.rotation_x = 180

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                temp = Vec3(mouse.normal.x, -mouse.normal.y, -mouse.normal.z)
                position = self.position + temp
                setdisplay(position.x, position.y, position.z)

            if key == 'right mouse down':
                global Data
                position = self.position
                Data[int(position.x)][int(position.y)][int(position.z)] = None
                destroy(self)

    def getData(self):
        return "DirtBlcck"

    def getProperties(self):
        return "None"

    def setProperties(self, STAT):
        if STAT == "None":
            self.interaction = STAT
            block.__init__(
                self,
                parent=scene,
                position=self.position,
                model='assets/block/dirt',
                texture=load_texture('assets/block/dirttexture.png'),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
        else:
            print("CLASS = DirtBlock :: WRONG STAT")


class GrassBlock(block):
    interaction = None
    electricity = False

    def __init__(self, position=(5, 2, 5)):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block/grass',
            texture=load_texture('assets/block/grasstexture.png'),
            origin_y=0.5,
            color=color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.lime,
        )
        self.rotation_x = 180

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                temp = Vec3(mouse.normal.x, -mouse.normal.y, -mouse.normal.z)
                position = self.position + temp
                setdisplay(position.x, position.y, position.z)

            if key == 'right mouse down':
                global Data
                position = self.position
                Data[int(position.x)][int(position.y)][int(position.z)] = None
                destroy(self)

    def getData(self):
        return "GrassBlcck"

    def getProperties(self):
        return "None"

    def setProperties(self, STAT):
        if STAT == "None":
            self.interaction = STAT
            block.__init__(
                self,
                parent=scene,
                position=self.position,
                model='assets/block/grass',
                texture=load_texture('assets/block/grasstexture.png'),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
        else:
            print("CLASS = GrassBlock :: WRONG STAT")


class IronBlock(block):
    interaction = None
    electricity = False

    def __init__(self, position=(5, 2, 5)):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block/Ironblock',
            texture=load_texture('assets/block/Ironblocktexture.png'),
            origin_y=0.5,
            color=color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.lime,
        )
        self.rotation_x = 180

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                temp = Vec3(mouse.normal.x, -mouse.normal.y, -mouse.normal.z)
                position = self.position + temp
                setdisplay(position.x, position.y, position.z)

        if key == 'right mouse down':
            global Data
            position = self.position
            Data[int(position.x)][int(position.y)][int(position.z)] = None
            destroy(self)

    def getData(self):
        return "IronBlcck"

    def getProperties(self):
        return "None"

    def setProperties(self, STAT):
        if STAT == "None":
            block.__init__(
                self,
                parent=scene,
                position=self.position,
                model='assets/block/Ironblock',
                texture=load_texture('assets/block/Ironblocktexture.png'),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
        else:
            print("CLASS = IronBlock :: WRONG STAT")


class LampBlock(block):
    LAMP_OFF = False
    LAMP_ON = True
    electricity = False

    interaction = LAMP_OFF

    def __init__(self, position=(5, 2, 5)):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block/redstonelamp',
            texture=load_texture('assets/block/redstonelamptexture.png'),
            origin_y=0.5,
            color=color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.lime,
        )
        self.rotation_x = 180

    def input(self, key):
        if self.hovered:
            # if key == 'z':
            #     self.interaction = not self.interaction
            #     if self.interaction:
            #         block.__init__(
            #             self,
            #             parent=scene,
            #             position=self.position,
            #             model='assets/block/redstonelampon',
            #             texture=load_texture('assets/block/redstonelampontexture.png'),
            #             origin_y=0.5,
            #             color=color.color(0, 0, random.uniform(.9, 1.0)),
            #             highlight_color=color.lime,
            #         )
            #         self.rotation_x = 180
            #     else:
            #         block.__init__(
            #             self,
            #             parent=scene,
            #             position=self.position,
            #             model='assets/block/redstonelamp',
            #             texture=load_texture('assets/block/redstonelamptexture.png'),
            #             origin_y=0.5,
            #             color=color.color(0, 0, random.uniform(.9, 1.0)),
            #             highlight_color=color.lime,
            #         )
            #         self.rotation_x = 180

            if key == 'left mouse down':
                temp = Vec3(mouse.normal.x, -mouse.normal.y, -mouse.normal.z)
                position = self.position + temp
                setdisplay(position.x, position.y, position.z)

            if key == 'right mouse down':
                global Data
                position = self.position
                Data[int(position.x)][int(position.y)][int(position.z)] = None
                destroy(self)

    def getData(self):
        return "LampBlock"

    def getProperties(self):
        if self.interaction == self.LAMP_OFF:
            return "LAMP_OFF"
        elif self.interaction == self.LAMP_ON:
            return "LAMP_ON"
        else:
            return "ERROR"

    def setProperties(self, STAT):
        if STAT == "LAMP_OFF":
            self.interaction = self.LAMP_OFF
            block.__init__(
                self,
                parent=scene,
                position=self.position,
                model='assets/block/redstonelamp',
                texture=load_texture('assets/block/redstonelamptexture.png'),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
        elif STAT == "LAMP_ON":
            self.interaction = self.LAMP_ON
            block.__init__(
                self,
                parent=scene,
                position=self.position,
                model='assets/block/redstonelampon',
                texture=load_texture('assets/block/redstonelampontexture.png'),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
        else:
            print("CLASS = lampblock :: WRONG STAT")


class Redstone(block):
    TICK9 = 9
    TICK8 = 8
    TICK7 = 7
    TICK6 = 6
    TICK5 = 5
    TICK4 = 4
    TICK3 = 3
    TICK2 = 2
    TICK1 = 1
    TICKOFF = 0

    interaction = TICKOFF

    def __init__(self, position=(5, 2, 5)):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block/redstone1',
            texture=load_texture('assets/block/redstonetexture1.png'),
            origin_y=0.5,
            color=color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.lime,
        )
        self.rotation_x = 180

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                temp = Vec3(mouse.normal.x, -mouse.normal.y, -mouse.normal.z)
                position = self.position + temp
                setdisplay(int(position.x), int(position.y), int(position.z))
            if key == 'right mouse down':
                global Data
                position = self.position
                Data[int(position.x)][int(position.y)][int(position.z)] = None
                Update.command.put(8, Update.tickcount, int(position.x), int(position.y), int(position.z))
                destroy(self)

    def getData(self):
        return "Redstone"

    def getProperties(self):
        if self.interaction == self.TICKOFF:
            return "TICKOFF"
        elif self.interaction == self.TICK1:
            return "TICK1"
        elif self.interaction == self.TICK2:
            return "TICK2"
        elif self.interaction == self.TICK3:
            return "TICK3"
        elif self.interaction == self.TICK4:
            return "TICK4"
        elif self.interaction == self.TICK5:
            return "TICK5"
        elif self.interaction == self.TICK6:
            return "TICK6"
        elif self.interaction == self.TICK7:
            return "TICK7"
        elif self.interaction == self.TICK8:
            return "TICK8"
        elif self.interaction == self.TICK9:
            return "TICK9"
        else:
            return "ERROR"

    def setProperties(self, STAT):
        position = self.position
        if STAT == "TICKOFF":
            self.interaction = self.TICKOFF
            block.__init__(
                self,
                parent=scene,
                position=position,
                model='assets/block/redstone1',
                texture=load_texture('assets/block/redstonetexture1.png'),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
        elif STAT == "TICK1":
            self.interaction = self.TICK1
            block.__init__(
                self,
                parent=scene,
                position=position,
                model='assets/block/redstone2',
                texture=load_texture('assets/block/redstonetexture2.png'),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
        elif STAT == "TICK2":
            self.interaction = self.TICK2
            block.__init__(
                self,
                parent=scene,
                position=position,
                model='assets/block/redstone3',
                texture=load_texture('assets/block/redstonetexture3.png'),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
        elif STAT == "TICK3":
            self.interaction = self.TICK3
            block.__init__(
                self,
                parent=scene,
                position=position,
                model='assets/block/redstone4',
                texture=load_texture('assets/block/redstonetexture4.png'),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
        elif STAT == "TICK4":
            self.interaction = self.TICK4
            block.__init__(
                self,
                parent=scene,
                position=position,
                model='assets/block/redstone5',
                texture=load_texture('assets/block/redstonetexture5.png'),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
        elif STAT == "TICK5":
            self.interaction = self.TICK5
            block.__init__(
                self,
                parent=scene,
                position=position,
                model='assets/block/redstone6',
                texture=load_texture('assets/block/redstonetexture6.png'),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
        elif STAT == "TICK6":
            self.interaction = self.TICK6
            block.__init__(
                self,
                parent=scene,
                position=position,
                model='assets/block/redstone7',
                texture=load_texture('assets/block/redstonetexture7.png'),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
        elif STAT == "TICK7":
            self.interaction = self.TICK7
            block.__init__(
                self,
                parent=scene,
                position=position,
                model='assets/block/redstone8',
                texture=load_texture('assets/block/redstonetexture8.png'),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
        elif STAT == "TICK8":
            self.interaction = self.TICK8
            block.__init__(
                self,
                parent=scene,
                position=position,
                model='assets/block/redstone9',
                texture=load_texture('assets/block/redstonetexture9.png'),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
        elif STAT == "TICK9":
            self.interaction = self.TICK9
            block.__init__(
                self,
                parent=scene,
                position=position,
                model='assets/block/redstone10',
                texture=load_texture('assets/block/redstonetexture10.png'),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
        else:
            print("CLASS = Redstone :: WRONG STAT")


class RedstoneBlock(block):
    interaction = None

    def __init__(self, position=(5, 2, 5)):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block/redstoneblock',
            texture=load_texture('assets/block/redstoneblocktexture.png'),
            origin_y=0.5,
            color=color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.lime,
        )
        self.rotation_x = 180

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                temp = Vec3(mouse.normal.x, -mouse.normal.y, -mouse.normal.z)
                position = self.position + temp
                setdisplay(position.x, position.y, position.z)

            if key == 'right mouse down':
                global Data
                position = self.position
                Data[int(position.x)][int(position.y)][int(position.z)] = None
                destroy(self)

    def getData(self):
        return "RedstoneBlock"

    def getProperties(self):
        return "None"

    def setProperties(self, STAT):
        if STAT == "None":
            block.__init__(
                self,
                parent=scene,
                position=self.position,
                model='assets/block/redstoneblock',
                texture=load_texture('assets/block/redstoneblocktexture.png'),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
        else:
            print("CLASS = RedstoneBlock :: WRONG STAT")


class Redstonetorch(block):
    TORCH_OFF = False
    TORCH_ON = True

    interaction = TORCH_ON

    def __init__(self, position=(5, 2, 5)):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block/torch',
            texture=load_texture('assets/block/torchtexture.png'),
            origin_y=0.5,
            color=color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.lime,
        )
        self.rotation_x = 180

    def input(self, key):
        if self.hovered:
            if key == 'z':
                self.interaction = not self.interaction
                if self.interaction:
                    block.__init__(
                        self,
                        parent=scene,
                        position=self.position,
                        model="assets/block/torchon",
                        texture=load_texture("assets/block/torchtextureon.png"),
                        origin_y=0.5,
                        color=color.color(0, 0, random.uniform(.9, 1.0)),
                        highlight_color=color.lime,
                    )
                    self.rotation_x = 180
                else:
                    block.__init__(
                        self,
                        parent=scene,
                        position=self.position,
                        model="assets/block/torch",
                        texture=load_texture("assets/block/torchtexture.png"),
                        origin_y=0.5,
                        color=color.color(0, 0, random.uniform(.9, 1.0)),
                        highlight_color=color.lime,
                    )
                    self.rotation_x = 180

            if key == 'left mouse down':
                position = self.position
                setdisplay(position.x, position.y, position.z)

            if key == 'right mouse down':
                global Data
                temp = Vec3(mouse.normal.x, -mouse.normal.y, -mouse.normal.z)
                position = self.position + temp
                Data[int(position.x)][int(position.y)][int(position.z)] = None
                destroy(self)

    def getData(self):
        return "Redstonetorch"

    def getProperties(self):
        if self.interaction == self.TORCH_OFF:
            return "TORCH_OFF"
        elif self.interaction == self.TORCH_ON:
            return "TORCH_ON"
        else:
            return "ERROR"

    def setProperties(self, STAT):
        if STAT == "TORCH_OFF":
            self.interaction = self.TORCH_OFF
            block.__init__(
                self,
                parent=scene,
                position=self.position,
                model="assets/block/torch",
                texture=load_texture("assets/block/torchtexture.png"),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
        elif STAT == "TORCH_ON":
            self.interaction = self.TORCH_ON
            block.__init__(
                self,
                parent=scene,
                position=self.position,
                model="assets/block/torchon",
                texture=load_texture("assets/block/torchtextureon.png"),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
        else:
            print("CLASS = Redstonetorch :: WRONG STAT")


class Repeater(block):
    REPEATEROFF_1 = ["OFF", 1]
    REPEATEROFF_2 = ["OFF", 2]
    REPEATEROFF_3 = ["OFF", 3]
    REPEATEROFF_4 = ["OFF", 4]
    REPEATERON_1 = ["ON", 1]
    REPEATERON_2 = ["ON", 2]
    REPEATERON_3 = ["ON", 3]
    REPEATERON_4 = ["ON", 4]

    interaction = REPEATEROFF_1
    Direction = 0

    def __init__(self, position=(5, 2, 5)):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block/repeateroff-1',
            texture=load_texture('assets/block/repeaterpoly.png'),
            origin_y=0.5,
            color=color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.lime,
        )
        self.rotation_x = 180
        self.rotation_y = self.Direction

    def input(self, key):
        if self.hovered:
            if key == 'z':
                self.changeSTAT()
                self.direction = self.rotation_y
            if key == 'left mouse down':
                temp = Vec3(mouse.normal.x, -mouse.normal.y, -mouse.normal.z)
                position = self.position + temp
                setdisplay(position.x, position.y, position.z)

            if key == 'right mouse down':
                global Data
                position = self.position
                Data[int(position.x)][int(position.y)][int(position.z)] = None
                destroy(self)

    def getData(self):
        return "Repeater"

    def getProperties(self):
        if self.interaction == self.REPEATEROFF_1:
            return "REPEATEROFF_1"
        elif self.interaction == self.REPEATEROFF_2:
            return "REPEATEROFF_2"
        elif self.interaction == self.REPEATEROFF_3:
            return "REPEATEROFF_3"
        elif self.interaction == self.REPEATEROFF_4:
            return "REPEATEROFF_4"
        elif self.interaction == self.REPEATERON_1:
            return "REPEATERON_1"
        elif self.interaction == self.REPEATERON_2:
            return "REPEATERON_2"
        elif self.interaction == self.REPEATERON_3:
            return "REPEATERON_3"
        elif self.interaction == self.REPEATERON_4:
            return "REPEATERON_4"
        else:
            return "ERROR"

    def setProperties(self, STAT):
        if STAT == "REPEATEROFF_1":
            self.interaction = self.REPEATEROFF_1
            block.__init__(
                self,
                parent=scene,
                position=self.position,
                model='assets/block/repeateroff-1',
                texture=load_texture('assets/block/repeaterpoly.png'),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
            self.rotation_y = self.Direction
        elif STAT == "REPEATEROFF_2":
            self.interaction = self.REPEATEROFF_2
            block.__init__(
                self,
                parent=scene,
                position=self.position,
                model='assets/block/repeateroff-2',
                texture=load_texture('assets/block/repeaterpoly.png'),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
            self.rotation_y = self.Direction
        elif STAT == "REPEATEROFF_3":
            self.interaction = self.REPEATEROFF_3
            block.__init__(
                self,
                parent=scene,
                position=self.position,
                model='assets/block/repeateroff-3',
                texture=load_texture('assets/block/repeaterpoly.png'),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
            self.rotation_y = self.Direction
        elif STAT == "REPEATEROFF_4":
            self.interaction = self.REPEATEROFF_4
            block.__init__(
                self,
                parent=scene,
                position=self.position,
                model='assets/block/repeateroff-4',
                texture=load_texture('assets/block/repeaterpoly.png'),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
            self.rotation_y = self.Direction
        elif STAT == "REPEATERON_1":
            self.interaction = self.REPEATERON_1
            block.__init__(
                self,
                parent=scene,
                position=self.position,
                model='assets/block/repeateron-1',
                texture=load_texture('assets/block/repeaterpolyon.png'),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
            self.rotation_y = self.Direction
        elif STAT == "REPEATERON_2":
            self.interaction = self.REPEATERON_2
            block.__init__(
                self,
                parent=scene,
                position=self.position,
                model='assets/block/repeateron-2',
                texture=load_texture('assets/block/repeaterpolyon.png'),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
            self.rotation_y = self.Direction
        elif STAT == "REPEATERON_3":
            self.interaction = self.REPEATERON_3
            block.__init__(
                self,
                parent=scene,
                position=self.position,
                model='assets/block/repeateron-3',
                texture=load_texture('assets/block/repeaterpolyon.png'),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
            self.rotation_y = self.Direction
        elif STAT == "REPEATERON_4":
            self.interaction = self.REPEATERON_4
            block.__init__(
                self,
                parent=scene,
                position=self.position,
                model='assets/block/repeateron-4',
                texture=load_texture('assets/block/repeaterpolyon.png'),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
            self.rotation_y = self.Direction
        else:
            print("CLASS = Repeater :: WRONG STAT")

    def changeSTAT(self):
        temp = [self.interaction[0], (self.interaction[1] + 1)]
        if temp[1] == 5:
            temp[1] = 1
        self.interaction = temp
        if temp == self.REPEATEROFF_1:
            self.setProperties("REPEATEROFF_1")
        elif temp == self.REPEATEROFF_2:
            self.setProperties("REPEATEROFF_2")
        elif temp == self.REPEATEROFF_3:
            self.setProperties("REPEATEROFF_3")
        elif temp == self.REPEATEROFF_4:
            self.setProperties("REPEATEROFF_4")
        elif temp == self.REPEATERON_1:
            self.setProperties("REPEATERON_1")
        elif temp == self.REPEATERON_2:
            self.setProperties("REPEATERON_2")
        elif temp == self.REPEATERON_3:
            self.setProperties("REPEATERON_3")
        elif temp == self.REPEATERON_4:
            self.setProperties("REPEATERON_4")
        return True

    def changeONOFF(self):
        temp = [self.interaction[0], self.interaction[1]]
        if temp[0]=="OFF":
            temp[0] = "ON"
        else:
            temp[0] = "OFF"

        self.interaction = temp
        if temp == self.REPEATEROFF_1:
            self.setProperties("REPEATEROFF_1")
        elif temp == self.REPEATEROFF_2:
            self.setProperties("REPEATEROFF_2")
        elif temp == self.REPEATEROFF_3:
            self.setProperties("REPEATEROFF_3")
        elif temp == self.REPEATEROFF_4:
            self.setProperties("REPEATEROFF_4")
        elif temp == self.REPEATERON_1:
            self.setProperties("REPEATERON_1")
        elif temp == self.REPEATERON_2:
            self.setProperties("REPEATERON_2")
        elif temp == self.REPEATERON_3:
            self.setProperties("REPEATERON_3")
        elif temp == self.REPEATERON_4:
            self.setProperties("REPEATERON_4")
        return True

class StoneBlock(block):
    interaction = None
    electricity = False

    def __init__(self, position=(5, 2, 5)):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block/stone',
            texture=load_texture('assets/block/stonetexture.png'),
            origin_y=0.5,
            color=color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.lime,
        )
        self.rotation_x = 180

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                temp = Vec3(mouse.normal.x, -mouse.normal.y, -mouse.normal.z)
                position = self.position + temp
                setdisplay(position.x, position.y, position.z)

            if key == 'right mouse down':
                global Data
                position = self.position
                Data[int(position.x)][int(position.y)][int(position.z)] = None
                destroy(self)

    def getData(self):
        return "StoneBlock"

    def getProperties(self):
        return "None"

    def setProperties(self, STAT):
        if STAT == "None":
            self.interaction = STAT
            block.__init__(
                self,
                parent=scene,
                position=self.position,
                model='assets/block/stone',
                texture=load_texture('assets/block/stonetexture.png'),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
        else:
            print("CLASS = StoneBlock :: WRONG STAT")


class Switch(block):
    SWITCH_OFF = False
    SWITCH_ON = True

    interaction = SWITCH_OFF

    def __init__(self, position=(5, 2, 5)):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block/switch',
            texture=load_texture('assets/block/switchtexture.png'),
            origin_y=0.5,
            color=color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.lime,
        )
        self.rotation_x = 180

    def input(self, key):
        if self.hovered:
            if key == 'z':
                self.interaction = not self.interaction
                if self.interaction:
                    block.__init__(
                        self,
                        parent=scene,
                        position=self.position,
                        model='assets/block/switchon',
                        texture=load_texture('assets/block/switchontexture.png'),
                        origin_y=0.5,
                        color=color.color(0, 0, random.uniform(.9, 1.0)),
                        highlight_color=color.lime,
                    )
                    self.rotation_x = 180
                else:
                    block.__init__(
                        self,
                        parent=scene,
                        position=self.position,
                        model='assets/block/switch',
                        texture=load_texture('assets/block/switchtexture.png'),
                        origin_y=0.5,
                        color=color.color(0, 0, random.uniform(.9, 1.0)),
                        highlight_color=color.lime,
                    )
                    self.rotation_x = 180

            if key == 'left mouse down':
                temp = Vec3(mouse.normal.x, -mouse.normal.y, -mouse.normal.z)
                position = self.position + temp
                setdisplay(position.x, position.y, position.z)

            if key == 'right mouse down':
                global Data
                position = self.position
                Data[int(position.x)][int(position.y)][int(position.z)] = None
                destroy(self)

    def getData(self):
        return "Switch"

    def getProperties(self):
        if self.interaction == self.SWITCH_OFF:
            return "SWITCH_OFF"
        elif self.interaction == self.SWITCH_ON:
            return "SWITCH_ON"
        else:
            return "ERROR"

    def setProperties(self, STAT):
        if STAT == "SWITCH_OFF":
            self.interaction = self.SWITCH_OFF
            super().__init__(
                parent=scene,
                position=self.position,
                model="assets/block/switch",
                texture=load_texture("assets/block/switchtexture.png"),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
        elif STAT == "SWITCH_ON":
            self.interaction = self.SWITCH_ON
            super().__init__(
                parent=scene,
                position=self.position,
                model="assets/block/switchon",
                texture=load_texture("assets/block/switchontexture.png"),
                origin_y=0.5,
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )
            self.rotation_x = 180
        else:
            print("CLASS = SWITCH :: WRONG STAT")


def setdisplay(x, y, z):
    global Data
    if Data[int(x)][int(y)][int(z)] is not None:
        print(Data[int(x)][int(y)][int(z)].getData())
        print("block is existing")
        return False

    if Inventory.selected == None:
        print("nothing selected")

    elif Inventory.selected == 1:
        Data[int(x)][int(y)][int(z)] = GrassBlock(position=(x, y, z))

    elif Inventory.selected == 2:
        Data[int(x)][int(y)][int(z)] = DirtBlock(position=(x, y, z))

    elif Inventory.selected == 3:
        Data[int(x)][int(y)][int(z)] = ButtonBlock(position=(x, y, z))

    elif Inventory.selected == 4:
        Data[int(x)][int(y)][int(z)] = IronBlock(position=(x, y, z))

    elif Inventory.selected == 5:
        Data[int(x)][int(y)][int(z)] = LampBlock(position=(x, y, z))
        Update.command.put(5, Update.tickcount, x, y, z)

    elif Inventory.selected == 6:
        Data[int(x)][int(y)][int(z)] = Redstone(position=(x, y, z))
        Update.command.put(4, Update.tickcount, x, y, z)

    elif Inventory.selected == 7:
        Data[int(x)][int(y)][int(z)] = RedstoneBlock(position=(x, y, z))
        Update.command.put(9, Update.tickcount, x, y, z)

    elif Inventory.selected == 8:
        Data[int(x)][int(y)][int(z)] = Redstonetorch(position=(x, y, z))

    elif Inventory.selected == 9:
        print()
        if UnityTab.player.position.x - x >= 0 and UnityTab.player.position.z - z >= 0:
            temp = Repeater(position=(x, y, z))
            temp.rotation_y = 0
            temp.Direction = 0
            Data[int(x)][int(y)][int(z)] = temp

        if UnityTab.player.position.x - x >= 0 and UnityTab.player.position.z - z < 0:
            temp = Repeater(position=(x, y, z))
            temp.rotation_y = 90
            temp.Direction = 90
            Data[int(x)][int(y)][int(z)] = temp

        if UnityTab.player.position.x - x < 0 and UnityTab.player.position.z - z < 0:
            temp = Repeater(position=(x, y, z))
            temp.rotation_y = 180
            temp.Direction = 180
            Data[int(x)][int(y)][int(z)] = temp

        if UnityTab.player.position.x - x < 0 and UnityTab.player.position.z - z >= 0:
            temp = Repeater(position=(x, y, z))
            temp.rotation_y = 270
            temp.Direction = 270
            Data[int(x)][int(y)][int(z)] = temp

        Update.command.put(6, Update.tickcount, x, y, z)

    elif Inventory.selected == 10:
        Data[int(x)][int(y)][int(z)] = StoneBlock(position=(x, y, z))

    elif Inventory.selected == 11:
        Data[int(x)][int(y)][int(z)] = Switch(position=(x, y, z))

    else:
        print("No such inventory")
        return False

    return True


class Queue:
    front = 0
    last = 0
    list = []

    def put(self, com, tick, x, y, z):
        self.list.append((com, tick, x, y, z))
        self.last += 1

    def peek(self):
        return self.list[self.front]

    def pop(self):
        self.list[self.front] = None
        self.front += 1

    def empty(self):
        if self.front == self.last:
            return True
        else:
            return False


class Update(threading.Thread):
    tickcount = 0
    command = Queue()

    def __init__(self):
        super().__init__()
        urs = UnityTab()
        

    def run(self):
        while True:
            Update.tickcount += 1

            while True:
                if self.command.empty():
                    break

                (com, tick, x, y, z) = self.command.peek()

                if tick > Update.tickcount:
                    break

                else:
                    # ToDo 레드스톤 -1
                    if com == 1:
                        Update.command.pop()

                        if Data[int(x)][int(y)][int(z)].getProperties() == "TICK9":
                            if Data[int(x + 1)][int(y)][int(z)] is not None:
                                if Data[int(x + 1)][int(y)][int(z)].getData() == "Redstone" and \
                                        Data[int(x + 1)][int(y)][int(z)].interaction < 9:
                                    Data[int(x + 1)][int(y)][int(z)].setProperties("TICK8")
                                    Update.command.put(1, Update.tickcount, x + 1, y, z)

                            if Data[int(x - 1)][int(y)][int(z)] is not None:
                                if Data[int(x - 1)][int(y)][int(z)].getData() == "Redstone" and \
                                        Data[int(x - 1)][int(y)][int(z)].interaction < 9:
                                    Data[int(x - 1)][int(y)][int(z)].setProperties("TICK8")
                                    Update.command.put(1, Update.tickcount, x - 1, y, z)
                            if Data[int(x)][int(y)][int(z + 1)] is not None:
                                if Data[int(x)][int(y)][int(z + 1)].getData() == "Redstone" and Data[int(x)][int(y)][
                                    int(z + 1)].interaction < 9:
                                    Data[int(x)][int(y)][int(z + 1)].setProperties("TICK8")
                                    Update.command.put(1, Update.tickcount, x, y, z + 1)

                            if Data[int(x)][int(y)][int(z - 1)] is not None:
                                if Data[int(x)][int(y)][int(z - 1)].getData() == "Redstone" and Data[int(x)][int(y)][
                                    int(z - 1)].interaction < 9:
                                    Data[int(x)][int(y)][int(z - 1)].setProperties("TICK8")
                                    Update.command.put(1, Update.tickcount, x, y, z - 1)
                        #############################################################################################
                        if Data[int(x)][int(y)][int(z)].getProperties() == "TICK8":
                            if Data[int(x + 1)][int(y)][int(z)] is not None:
                                if Data[int(x + 1)][int(y)][int(z)].getData() == "Redstone" and \
                                        Data[int(x + 1)][int(y)][int(z)].interaction < 8:
                                    Data[int(x + 1)][int(y)][int(z)].setProperties("TICK7")
                                    Update.command.put(1, Update.tickcount, x + 1, y, z)

                            if Data[int(x - 1)][int(y)][int(z)] is not None:
                                if Data[int(x - 1)][int(y)][int(z)].getData() == "Redstone" and \
                                        Data[int(x - 1)][int(y)][int(z)].interaction < 8:
                                    Data[int(x - 1)][int(y)][int(z)].setProperties("TICK7")
                                    Update.command.put(1, Update.tickcount, x - 1, y, z)

                            if Data[int(x)][int(y)][int(z + 1)] is not None:
                                if Data[int(x)][int(y)][int(z + 1)].getData() == "Redstone" and Data[int(x)][int(y)][
                                    int(z + 1)].interaction < 8:
                                    Data[int(x)][int(y)][int(z + 1)].setProperties("TICK7")
                                    Update.command.put(1, Update.tickcount, x, y, z + 1)

                            if Data[int(x)][int(y)][int(z - 1)] is not None:
                                if Data[int(x)][int(y)][int(z - 1)].getData() == "Redstone" and Data[int(x)][int(y)][
                                    int(z - 1)].interaction < 8:
                                    Data[int(x)][int(y)][int(z - 1)].setProperties("TICK7")
                                    Update.command.put(1, Update.tickcount, x, y, z - 1)
                        #############################################################################################
                        if Data[int(x)][int(y)][int(z)].getProperties() == "TICK7":
                            if Data[int(x + 1)][int(y)][int(z)] is not None:
                                if Data[int(x + 1)][int(y)][int(z)].getData() == "Redstone" and \
                                        Data[int(x + 1)][int(y)][int(z)].interaction < 7:
                                    Data[int(x + 1)][int(y)][int(z)].setProperties("TICK6")
                                    Update.command.put(1, Update.tickcount, x + 1, y, z)

                            if Data[int(x - 1)][int(y)][int(z)] is not None:
                                if Data[int(x - 1)][int(y)][int(z)].getData() == "Redstone" and \
                                        Data[int(x - 1)][int(y)][int(z)].interaction < 7:
                                    Data[int(x - 1)][int(y)][int(z)].setProperties("TICK6")
                                    Update.command.put(1, Update.tickcount, x - 1, y, z)

                            if Data[int(x)][int(y)][int(z + 1)] is not None:
                                if Data[int(x)][int(y)][int(z + 1)].getData() == "Redstone" and \
                                        Data[int(x)][int(y)][int(z + 1)].interaction < 7:
                                    Data[int(x)][int(y)][int(z + 1)].setProperties("TICK6")
                                    Update.command.put(1, Update.tickcount, x, y, z + 1)

                            if Data[int(x)][int(y)][int(z - 1)] is not None:
                                if Data[int(x)][int(y)][int(z - 1)].getData() == "Redstone" and \
                                        Data[int(x)][int(y)][int(z - 1)].interaction < 7:
                                    Data[int(x)][int(y)][int(z - 1)].setProperties("TICK6")
                                    Update.command.put(1, Update.tickcount, x, y, z - 1)
                        #############################################################################################
                        if Data[int(x)][int(y)][int(z)].getProperties() == "TICK6":
                            if Data[int(x + 1)][int(y)][int(z)] is not None:
                                if Data[int(x + 1)][int(y)][int(z)].getData() == "Redstone" and \
                                        Data[int(x + 1)][int(y)][int(z)].interaction < 6:
                                    Data[int(x + 1)][int(y)][int(z)].setProperties("TICK5")
                                    Update.command.put(1, Update.tickcount, x + 1, y, z)

                            if Data[int(x - 1)][int(y)][int(z)] is not None:
                                if Data[int(x - 1)][int(y)][int(z)].getData() == "Redstone" and \
                                        Data[int(x - 1)][int(y)][int(z)].interaction < 6:
                                    Data[int(x - 1)][int(y)][int(z)].setProperties("TICK5")
                                    Update.command.put(1, Update.tickcount, x - 1, y, z)

                            if Data[int(x)][int(y)][int(z + 1)] is not None:
                                if Data[int(x)][int(y)][int(z + 1)].getData() == "Redstone" and \
                                        Data[int(x)][int(y)][int(z + 1)].interaction < 6:
                                    Data[int(x)][int(y)][int(z + 1)].setProperties("TICK5")
                                    Update.command.put(1, Update.tickcount, x, y, z + 1)

                            if Data[int(x)][int(y)][int(z - 1)] is not None:
                                if Data[int(x)][int(y)][int(z - 1)].getData() == "Redstone" and \
                                        Data[int(x)][int(y)][int(z - 1)].interaction < 6:
                                    Data[int(x)][int(y)][int(z - 1)].setProperties("TICK5")
                                    Update.command.put(1, Update.tickcount, x, y, z - 1)
                        #############################################################################################
                        if Data[int(x)][int(y)][int(z)].getProperties() == "TICK5":
                            if Data[int(x + 1)][int(y)][int(z)] is not None:
                                if Data[int(x + 1)][int(y)][int(z)].getData() == "Redstone" and \
                                        Data[int(x + 1)][int(y)][int(z)].interaction < 5:
                                    Data[int(x + 1)][int(y)][int(z)].setProperties("TICK4")
                                    Update.command.put(1, Update.tickcount, x + 1, y, z)

                            if Data[int(x - 1)][int(y)][int(z)] is not None:
                                if Data[int(x - 1)][int(y)][int(z)].getData() == "Redstone" and \
                                        Data[int(x - 1)][int(y)][int(z)].interaction < 5:
                                    Data[int(x - 1)][int(y)][int(z)].setProperties("TICK4")
                                    Update.command.put(1, Update.tickcount, x - 1, y, z)

                            if Data[int(x)][int(y)][int(z + 1)] is not None:
                                if Data[int(x)][int(y)][int(z + 1)].getData() == "Redstone" and \
                                        Data[int(x)][int(y)][int(z + 1)].interaction < 5:
                                    Data[int(x)][int(y)][int(z + 1)].setProperties("TICK4")
                                    Update.command.put(1, Update.tickcount, x, y, z + 1)

                            if Data[int(x)][int(y)][int(z - 1)] is not None:
                                if Data[int(x)][int(y)][int(z - 1)].getData() == "Redstone" and \
                                        Data[int(x)][int(y)][int(z - 1)].interaction < 5:
                                    Data[int(x)][int(y)][int(z - 1)].setProperties("TICK4")
                                    Update.command.put(1, Update.tickcount, x, y, z - 1)
                        ############################################################################################
                        if Data[int(x)][int(y)][int(z)].getProperties() == "TICK4":
                            if Data[int(x + 1)][int(y)][int(z)] is not None:
                                if Data[int(x + 1)][int(y)][int(z)].getData() == "Redstone" and \
                                        Data[int(x + 1)][int(y)][int(z)].interaction < 4:
                                    Data[int(x + 1)][int(y)][int(z)].setProperties("TICK3")
                                    Update.command.put(1, Update.tickcount, x + 1, y, z)

                            if Data[int(x - 1)][int(y)][int(z)] is not None:
                                if Data[int(x - 1)][int(y)][int(z)].getData() == "Redstone" and \
                                        Data[int(x - 1)][int(y)][int(z)].interaction < 4:
                                    Data[int(x - 1)][int(y)][int(z)].setProperties("TICK3")
                                    Update.command.put(1, Update.tickcount, x - 1, y, z)

                            if Data[int(x)][int(y)][int(z + 1)] is not None:
                                if Data[int(x)][int(y)][int(z + 1)].getData() == "Redstone" and \
                                        Data[int(x)][int(y)][int(z + 1)].interaction < 4:
                                    Data[int(x)][int(y)][int(z + 1)].setProperties("TICK3")
                                    Update.command.put(1, Update.tickcount, x, y, z + 1)

                            if Data[int(x)][int(y)][int(z - 1)] is not None:
                                if Data[int(x)][int(y)][int(z - 1)].getData() == "Redstone" and \
                                        Data[int(x)][int(y)][int(z - 1)].interaction < 4:
                                    Data[int(x)][int(y)][int(z - 1)].setProperties("TICK3")
                                    Update.command.put(1, Update.tickcount, x, y, z - 1)
                        ####################################################################################
                        if Data[int(x)][int(y)][int(z)].getProperties() == "TICK3":
                            if Data[int(x + 1)][int(y)][int(z)] is not None:
                                if Data[int(x + 1)][int(y)][int(z)].getData() == "Redstone" and \
                                        Data[int(x + 1)][int(y)][int(z)].interaction < 3:
                                    Data[int(x + 1)][int(y)][int(z)].setProperties("TICK2")
                                    Update.command.put(1, Update.tickcount, x + 1, y, z)

                            if Data[int(x - 1)][int(y)][int(z)] is not None:
                                if Data[int(x - 1)][int(y)][int(z)].getData() == "Redstone" and \
                                        Data[int(x - 1)][int(y)][int(z)].interaction < 3:
                                    Data[int(x - 1)][int(y)][int(z)].setProperties("TICK2")
                                    Update.command.put(1, Update.tickcount, x - 1, y, z)

                            if Data[int(x)][int(y)][int(z + 1)] is not None:
                                if Data[int(x)][int(y)][int(z + 1)].getData() == "Redstone" and \
                                        Data[int(x)][int(y)][int(z + 1)].interaction < 3:
                                    Data[int(x)][int(y)][int(z + 1)].setProperties("TICK2")
                                    Update.command.put(1, Update.tickcount, x, y, z + 1)

                            if Data[int(x)][int(y)][int(z - 1)] is not None:
                                if Data[int(x)][int(y)][int(z - 1)].getData() == "Redstone" and \
                                        Data[int(x)][int(y)][int(z - 1)].interaction < 3:
                                    Data[int(x)][int(y)][int(z - 1)].setProperties("TICK2")
                                    Update.command.put(1, Update.tickcount, x, y, z - 1)
                        ########################################################################################
                        if Data[int(x)][int(y)][int(z)].getProperties() == "TICK2":
                            if Data[int(x + 1)][int(y)][int(z)] is not None:
                                if Data[int(x + 1)][int(y)][int(z)].getData() == "Redstone" and \
                                        Data[int(x + 1)][int(y)][int(z)].interaction < 2:
                                    Data[int(x + 1)][int(y)][int(z)].setProperties("TICK1")
                                    Update.command.put(1, Update.tickcount, x + 1, y, z)

                            if Data[int(x - 1)][int(y)][int(z)] is not None:
                                if Data[int(x - 1)][int(y)][int(z)].getData() == "Redstone" and \
                                        Data[int(x - 1)][int(y)][int(z)].interaction < 2:
                                    Data[int(x - 1)][int(y)][int(z)].setProperties("TICK1")
                                    Update.command.put(1, Update.tickcount, x - 1, y, z)

                            if Data[int(x)][int(y)][int(z + 1)] is not None:
                                if Data[int(x)][int(y)][int(z + 1)].getData() == "Redstone" and \
                                        Data[int(x)][int(y)][int(z + 1)].interaction < 2:
                                    Data[int(x)][int(y)][int(z + 1)].setProperties("TICK1")
                                    Update.command.put(1, Update.tickcount + 1, x, y, z + 1)

                            if Data[int(x)][int(y)][int(z - 1)] is not None:
                                if Data[int(x)][int(y)][int(z - 1)].getData() == "Redstone" and \
                                        Data[int(x)][int(y)][int(z - 1)].interaction < 2:
                                    Data[int(x)][int(y)][int(z - 1)].setProperties("TICK1")
                                    Update.command.put(1, Update.tickcount, x, y, z - 1)
                        ############################################################################################
                        if Data[int(x)][int(y)][int(z)].getProperties() == "TICK1":
                            if Data[int(x + 1)][int(y)][int(z)] is not None:
                                if Data[int(x + 1)][int(y)][int(z)].getData() == "Redstone" and \
                                        Data[int(x + 1)][int(y)][int(z)].interaction < 1:
                                    Data[int(x + 1)][int(y)][int(z)].setProperties("TICKOFF")
                                    Update.command.put(1, Update.tickcount, x + 1, y, z)

                            if Data[int(x - 1)][int(y)][int(z)] is not None:
                                if Data[int(x - 1)][int(y)][int(z)].getData() == "Redstone" and \
                                        Data[int(x - 1)][int(y)][int(z)].interaction < 1:
                                    Data[int(x - 1)][int(y)][int(z)].setProperties("TICKOFF")
                                    Update.command.put(1, Update.tickcount, x - 1, y, z)

                            if Data[int(x)][int(y)][int(z + 1)] is not None:
                                if Data[int(x)][int(y)][int(z + 1)].getData() == "Redstone" and \
                                        Data[int(x)][int(y)][int(z + 1)].interaction < 1:
                                    Data[int(x)][int(y)][int(z + 1)].setProperties("TICKOFF")
                                    Update.command.put(1, Update.tickcount, x, y, z + 1)

                            if Data[int(x)][int(y)][int(z - 1)] is not None:
                                if Data[int(x)][int(y)][int(z - 1)].getData() == "Redstone" and \
                                        Data[int(x)][int(y)][int(z - 1)].interaction < 1:
                                    Data[int(x)][int(y)][int(z - 1)].setProperties("TICKOFF")
                                    Update.command.put(1, Update.tickcount, x, y, z - 1)

                        if Data[int(x + 1)][int(y)][int(z)] is not None:
                            if Data[int(x + 1)][int(y)][int(z)].getData() == "LampBlock":
                                Update.command.put(5, Update.tickcount, x + 1, y, z)

                        if Data[int(x - 1)][int(y)][int(z)] is not None:
                            if Data[int(x - 1)][int(y)][int(z)].getData() == "LampBlock":
                                Update.command.put(5, Update.tickcount, x - 1, y, z)

                        if Data[int(x)][int(y)][int(z + 1)] is not None:
                            if Data[int(x)][int(y)][int(z + 1)].getData() == "LampBlock":
                                Update.command.put(5, Update.tickcount, x, y, z + 1)

                        if Data[int(x)][int(y)][int(z - 1)] is not None:
                            if Data[int(x)][int(y)][int(z - 1)].getData() == "LampBlock":
                                Update.command.put(5, Update.tickcount, x, y, z - 1)
                        ############################################################################

                        if Data[int(x + 1)][int(y)][int(z)] is not None:
                            print(1)
                            if Data[int(x + 1)][int(y)][int(z)].getData() == "Repeater" and Data[int(x + 1)][int(y)][int(z)].Direction == 180:
                                print(1)
                                Update.command.put(6, Update.tickcount, x + 1, y, z)

                        if Data[int(x - 1)][int(y)][int(z)] is not None:
                            print(2)
                            if Data[int(x - 1)][int(y)][int(z)].getData() == "Repeater" and Data[int(x - 1)][int(y)][int(z)].Direction == 0:
                                print(2)
                                Update.command.put(6, Update.tickcount, x - 1, y, z)

                        if Data[int(x)][int(y)][int(z + 1)] is not None:
                            print(3)
                            if Data[int(x)][int(y)][int(z + 1)].getData() == "Repeater" and Data[int(x)][int(y)][int(z+1)].Direction == 90:
                                print(3)
                                Update.command.put(6, Update.tickcount, x, y, z + 1)

                        if Data[int(x)][int(y)][int(z - 1)] is not None:
                            print(4)
                            if Data[int(x)][int(y)][int(z - 1)].getData() == "Repeater" and Data[int(x)][int(y)][int(z-1)].Direction == 270:
                                print(4)
                                Update.command.put(6, Update.tickcount, x, y, z - 1)

                        print("command1")

                    # ToDo 레드스톤 풀차지
                    elif com == 2:
                        Update.command.pop()
                        Data[int(x)][int(y)][int(z)].setProperties("TICK9")

                        if Data[int(x + 1)][int(y)][int(z)] is not None:
                            if Data[int(x + 1)][int(y)][int(z)].getData() == "Redstone":
                                Update.command.put(1, Update.tickcount, x, y, z)
                            if Data[int(x + 1)][int(y)][int(z)].getData() == "LampBlock":
                                Update.command.put(5, Update.tickcount, x+1, y, z)

                        if Data[int(x - 1)][int(y)][int(z)] is not None:
                            if Data[int(x - 1)][int(y)][int(z)].getData() == "Redstone":
                                Update.command.put(1, Update.tickcount, x, y, z)
                            if Data[int(x - 1)][int(y)][int(z)].getData() == "LampBlock":
                                Update.command.put(5, Update.tickcount, x-1, y, z)

                        if Data[int(x)][int(y)][int(z + 1)] is not None:
                            if Data[int(x)][int(y)][int(z + 1)].getData() == "Redstone":
                                Update.command.put(1, Update.tickcount, x, y, z)
                            if Data[int(x)][int(y)][int(z + 1)].getData() == "LampBlock":
                                Update.command.put(5, Update.tickcount, x, y, z+1)

                        if Data[int(x)][int(y)][int(z - 1)] is not None:
                            if Data[int(x)][int(y)][int(z - 1)].getData() == "Redstone":
                                Update.command.put(1, Update.tickcount, x, y, z)
                            if Data[int(x)][int(y)][int(z - 1)].getData() == "LampBlock":
                                Update.command.put(5, Update.tickcount, x, y, z-1)

                        print("command2")

                    # ToDo 블럭 전기 들어옴 + 주변 블럭 신호 보내기
                    elif com == 3:
                        print("command3")

                    # ToDo 블럭 주변 전기 공급원 확인, 처리
                    elif com == 4:
                        Update.command.pop()

                        if Data[int(x)][int(y)][int(z)] is not None:
                            if Data[int(x)][int(y)][int(z)].getData() == "Redstone":

                                if Data[int(x + 1)][int(y)][int(z)] is not None:
                                    if Data[int(x + 1)][int(y)][int(z)].getData() == "Redstone":
                                        Update.command.put(1, Update.tickcount, x + 1, y, z)
                                    if Data[int(x + 1)][int(y)][int(z)].getData() == "RedstoneBlock":
                                        Update.command.put(2, Update.tickcount, x, y, z)

                                if Data[int(x - 1)][int(y)][int(z)] is not None:
                                    if Data[int(x - 1)][int(y)][int(z)].getData() == "Redstone":
                                        Update.command.put(1, Update.tickcount, x - 1, y, z)
                                    if Data[int(x - 1)][int(y)][int(z)].getData() == "RedstoneBlock":
                                        print(2)
                                        Update.command.put(2, Update.tickcount, x, y, z)

                                if Data[int(x)][int(y)][int(z + 1)] is not None:
                                    if Data[int(x)][int(y)][int(z + 1)].getData() == "Redstone":
                                        Update.command.put(1, Update.tickcount, x, y, z + 1)
                                    if Data[int(x)][int(y)][int(z + 1)].getData() == "RedstoneBlock":
                                        print(3)
                                        Update.command.put(2, Update.tickcount, x, y, z)

                                if Data[int(x)][int(y)][int(z - 1)] is not None:
                                    if Data[int(x)][int(y)][int(z - 1)].getData() == "Redstone":
                                        Update.command.put(1, Update.tickcount, x, y, z - 1)
                                    if Data[int(x)][int(y)][int(z - 1)].getData() == "RedstoneBlock":
                                        print(4)
                                        Update.command.put(2, Update.tickcount, x, y, z)

                        print("command4")

                    # ToDo 레드스톤 램프 ON & 확인
                    elif com == 5:
                        Update.command.pop()

                        if Data[int(x + 1)][int(y)][int(z)] is not None:
                            if Data[int(x + 1)][int(y)][int(z)].getData() == "Redstone" and Data[int(x + 1)][int(y)][int(z)].interaction >=1:
                                Data[int(x)][int(y)][int(z)].setProperties("LAMP_ON")
                            if Data[int(x + 1)][int(y)][int(z)].getData() == "RedstoneBlock":
                                    Data[int(x)][int(y)][int(z)].setProperties("LAMP_ON")
                            if Data[int(x + 1)][int(y)][int(z)].getData() == "Repeater" and Data[int(x + 1)][int(y)][int(z)].interaction[0]=="ON":
                                    Data[int(x)][int(y)][int(z)].setProperties("LAMP_ON")

                        elif Data[int(x - 1)][int(y)][int(z)] is not None:
                            if Data[int(x - 1)][int(y)][int(z)].getData() == "Redstone" and Data[int(x - 1)][int(y)][int(z)].interaction >=1:
                                Data[int(x)][int(y)][int(z)].setProperties("LAMP_ON")
                            if Data[int(x - 1)][int(y)][int(z)].getData() == "RedstoneBlock":
                                Data[int(x)][int(y)][int(z)].setProperties("LAMP_ON")
                            if Data[int(x - 1)][int(y)][int(z)].getData() == "Repeater" and Data[int(x - 1)][int(y)][int(z)].interaction[0]=="ON":
                                Data[int(x)][int(y)][int(z)].setProperties("LAMP_ON")

                        elif Data[int(x)][int(y)][int(z + 1)] is not None:
                            if Data[int(x)][int(y)][int(z + 1)].getData() == "Redstone" and Data[int(x)][int(y)][int(z+1)].interaction >=1:
                                Data[int(x)][int(y)][int(z)].setProperties("LAMP_ON")
                            if Data[int(x)][int(y)][int(z + 1)].getData() == "RedstoneBlock":
                                Data[int(x)][int(y)][int(z)].setProperties("LAMP_ON")
                            if Data[int(x)][int(y)][int(z+1)].getData() == "Repeater" and Data[int(x)][int(y)][int(z+1)].interaction[0]=="ON":
                                Data[int(x)][int(y)][int(z)].setProperties("LAMP_ON")

                        elif Data[int(x)][int(y)][int(z - 1)] is not None:
                            if Data[int(x)][int(y)][int(z - 1)].getData() == "Redstone" and Data[int(x)][int(y)][int(z-1)].interaction >=1:
                                Data[int(x)][int(y)][int(z)].setProperties("LAMP_ON")
                            if Data[int(x)][int(y)][int(z - 1)].getData() == "RedstoneBlock":
                                Data[int(x)][int(y)][int(z)].setProperties("LAMP_ON")
                            if Data[int(x)][int(y)][int(z - 1)].getData() == "Repeater" and Data[int(x)][int(y)][int(z - 1)].interaction[0] == "ON":
                                Data[int(x)][int(y)][int(z)].setProperties("LAMP_ON")

                        else:
                            Data[int(x)][int(y)][int(z)].setProperties("LAMP_OFF")

                        print("command5")

                    # ToDo 리피터 지연 & 옆 전류 확인
                    elif com == 6:
                        Update.command.pop()

                        if Data[int(x - 1)][int(y)][int(z)] is not None:
                            if Data[int(x - 1)][int(y)][int(z)].getData() == "Redstone" and Data[int(x - 1)][int(y)][int(z)].interaction >= 1 and Data[int(x)][int(y)][int(z)].Direction == 180:
                                Data[int(x)][int(y)][int(z)].changeONOFF()
                                if Data[int(x + 1)][int(y)][int(z)] is not None:
                                  if Data[int(x + 1)][int(y)][int(z)].getData() == "Redstone":
                                      Update.command.put(2, Update.tickcount+Data[int(x)][int(y)][int(z)].interaction[1], x+1, y, z)
                                  if Data[int(x + 1)][int(y)][int(z)].getData() == "LampBlock":
                                      Update.command.put(5,Update.tickcount + Data[int(x)][int(y)][int(z)].interaction[1],x + 1, y, z)

                            if Data[int(x - 1)][int(y)][int(z)].getData() == "RedstoneBlock" and Data[int(x)][int(y)][int(z)].Direction == 180:
                                Data[int(x)][int(y)][int(z)].changeONOFF()
                                if Data[int(x + 1)][int(y)][int(z)] is not None:
                                  if Data[int(x + 1)][int(y)][int(z)].getData() == "Redstone":
                                      Update.command.put(2, Update.tickcount+Data[int(x)][int(y)][int(z)].interaction[1], x+1, y, z)
                                  if Data[int(x + 1)][int(y)][int(z)].getData() == "LampBlock":
                                      Update.command.put(5,Update.tickcount + Data[int(x)][int(y)][int(z)].interaction[1],x + 1, y, z)

                        if Data[int(x + 1)][int(y)][int(z)] is not None:
                            if Data[int(x+1)][int(y)][int(z)].getData() == "Redstone" and Data[int(x + 1)][int(y)][int(z)].interaction >= 1 and Data[int(x)][int(y)][int(z)].Direction == 0:
                                Data[int(x)][int(y)][int(z)].changeONOFF()
                                if Data[int(x - 1)][int(y)][int(z)] is not None:
                                  if Data[int(x - 1)][int(y)][int(z)].getData() == "Redstone":
                                    Update.command.put(2, Update.tickcount+Data[int(x)][int(y)][int(z)].interaction[1], x-1, y, z)
                                  if Data[int(x - 1)][int(y)][int(z)].getData() == "LampBlock":
                                    Update.command.put(5, Update.tickcount+Data[int(x)][int(y)][int(z)].interaction[1], x-1, y, z)

                            if Data[int(x+1)][int(y)][int(z)].getData() == "RedstoneBlock" and Data[int(x)][int(y)][int(z)].Direction == 0:
                                Data[int(x)][int(y)][int(z)].changeONOFF()
                                if Data[int(x - 1)][int(y)][int(z)] is not None:
                                  if Data[int(x - 1)][int(y)][int(z)].getData() == "Redstone":
                                    Update.command.put(2, Update.tickcount+Data[int(x)][int(y)][int(z)].interaction[1], x-1, y, z)
                                  if Data[int(x - 1)][int(y)][int(z)].getData() == "LampBlock":
                                    Update.command.put(5, Update.tickcount+Data[int(x)][int(y)][int(z)].interaction[1], x-1, y, z)

                        if Data[int(x)][int(y)][int(z - 1)] is not None:
                            if Data[int(x)][int(y)][int(z - 1)].getData() == "Redstone" and Data[int(x )][int(y)][int(z-1)].interaction >= 1 and Data[int(x)][int(y)][int(z)].Direction == 90:
                                Data[int(x)][int(y)][int(z)].changeONOFF()
                                if Data[int(x)][int(y)][int(z + 1)] is not None:
                                  if Data[int(x)][int(y)][int(z+1)].getData() == "Redstone":
                                    Update.command.put(2, Update.tickcount+Data[int(x)][int(y)][int(z)].interaction[1], x, y, z+1)
                                  if Data[int(x)][int(y)][int(z+1)].getData() == "LampBlock":
                                    Update.command.put(5, Update.tickcount+Data[int(x)][int(y)][int(z)].interaction[1], x, y, z+1)

                            if Data[int(x)][int(y)][int(z - 1)].getData() == "RedstoneBlock" and Data[int(x)][int(y)][int(z)].Direction == 90:
                                Data[int(x)][int(y)][int(z)].changeONOFF()
                                if Data[int(x)][int(y)][int(z + 1)] is not None:
                                  if Data[int(x)][int(y)][int(z+1)].getData() == "Redstone":
                                    Update.command.put(2, Update.tickcount+Data[int(x)][int(y)][int(z)].interaction[1], x, y, z+1)
                                  if Data[int(x)][int(y)][int(z+1)].getData() == "LampBlock":
                                    Update.command.put(5, Update.tickcount+Data[int(x)][int(y)][int(z)].interaction[1], x, y, z+1)

                        if Data[int(x)][int(y)][int(z + 1)] is not None:
                            if Data[int(x)][int(y)][int(z + 1)].getData() == "Redstone" and Data[int(x )][int(y)][int(z+1)].interaction >= 1 and Data[int(x)][int(y)][int(z)].Direction == 270:
                                Data[int(x)][int(y)][int(z)].changeONOFF()
                                if Data[int(x)][int(y)][int(z - 1)] is not None:
                                  if Data[int(x)][int(y)][int(z-1)].getData() == "Redstone":
                                    Update.command.put(2, Update.tickcount+Data[int(x)][int(y)][int(z)].interaction[1], x, y, z-1)
                                  if Data[int(x)][int(y)][int(z-1)].getData() == "LampBlock":
                                    Update.command.put(5, Update.tickcount+Data[int(x)][int(y)][int(z)].interaction[1], x, y, z-1)
                            if Data[int(x)][int(y)][int(z + 1)].getData() == "RedstoneBlock"and Data[int(x)][int(y)][int(z)].Direction == 270:
                                Data[int(x)][int(y)][int(z)].changeONOFF()
                                if Data[int(x)][int(y)][int(z - 1)] is not None:
                                  if Data[int(x)][int(y)][int(z-1)].getData() == "Redstone":
                                    Update.command.put(2, Update.tickcount+Data[int(x)][int(y)][int(z)].interaction[1], x, y, z-1)
                                  if Data[int(x)][int(y)][int(z-1)].getData() == "LampBlock":
                                    Update.command.put(5, Update.tickcount+Data[int(x)][int(y)][int(z)].interaction[1], x, y, z-1)

                        print("command6")

                    # ToDo 레드스톤 토치 온 오프
                    elif com == 7:
                        print("command7")

                    # ToDo 레드스톤 꺼짐
                    elif com == 8:
                        Update.command.pop()
                        for i in range(-50, 50, 1):
                            for j in range(-50, 50, 1):
                                for k in range(-50, 50, 1):
                                    if Data[int(i)][int(j)][int(k)] is not None:
                                        if Data[int(i)][int(j)][int(k)].getName() == "Redstone":
                                            Data[int(i)][int(j)][int(k)].setProperties("TICKOFF")

                        for i in range(-50, 50, 1):
                            for j in range(-50, 50, 1):
                                for k in range(-50, 50, 1):
                                    if Data[int(i)][int(j)][int(k)] is not None:
                                        if Data[int(i)][int(j)][int(k)].getName() == "RedstoneBlock":
                                            Update.command.put(9, Update.tickcount, i, j, k)

                        print("command8")

                    # ToDo 전류 공급원 설치
                    elif com == 9:
                        Update.command.pop()

                        if Data[int(x + 1)][int(y)][int(z)] is not None:
                            if Data[int(x + 1)][int(y)][int(z)].getData() == "Redstone":
                                Update.command.put(2, Update.tickcount, x + 1, y, z)
                            if Data[int(x + 1)][int(y)][int(z)].getData() == "Repeater":
                                Update.command.put(6, Update.tickcount, x + 1, y, z)

                        if Data[int(x - 1)][int(y)][int(z)] is not None:
                            if Data[int(x - 1)][int(y)][int(z)].getData() == "Redstone":
                                Update.command.put(2, Update.tickcount, x - 1, y, z)
                            if Data[int(x - 1)][int(y)][int(z)].getData() == "Repeater":
                                Update.command.put(6, Update.tickcount, x - 1, y, z)

                        if Data[int(x)][int(y)][int(z + 1)] is not None:
                            if Data[int(x)][int(y)][int(z + 1)].getData() == "Redstone":
                                Update.command.put(2, Update.tickcount, x, y, z + 1)
                            if Data[int(x)][int(y)][int(z + 1)].getData() == "Repeater":
                                Update.command.put(6, Update.tickcount, x, y, z + 1)

                        if Data[int(x)][int(y)][int(z - 1)] is not None:
                            if Data[int(x)][int(y)][int(z - 1)].getData() == "Redstone":
                                Update.command.put(2, Update.tickcount, x, y, z - 1)
                            if Data[int(x)][int(y)][int(z - 1)].getData() == "Repeater":
                                Update.command.put(6, Update.tickcount, x, y, z - 1)

                        print("command9")

                    # ToDo 버튼 눌림
                    elif com == 10:
                        print("command10")

                    # ToDo 버튼 꺼짐:
                    elif com == 11:
                        print("command11")

                    # ToDo 스위치 눌림
                    elif com == 12:
                        print("command10")

                    # ToDo 스위치 꺼짐:
                    elif com == 13:
                        print("command11")

                    else:
                        print("no such command")

            time.sleep(1)
