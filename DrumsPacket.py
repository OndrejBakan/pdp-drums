import vgamepad as vg


class DrumsPacket:
    POS_PAD = 8
    POS_PEDAL = 10
    POS_DPAD = 11

    POS_GUIDE = 31
    POS_START = POS_BACK = 9

    VAL_PAD_RED = 2
    VAL_PAD_YELLOW = 8
    VAL_PAD_BLUE = 4
    VAL_PAD_GREEN = 1

    VAL_PEDAL_ONE = 1
    VAL_PEDAL_TWO = 2

    VAL_DPAD_UP = 1
    VAL_DPAD_DOWN = 2 
    VAL_DPAD_LEFT = 4
    VAL_DPAD_RIGHT = 8

    VAL_GUIDE = 1
    VAL_START = 4
    VAL_BACK = 8
   
    VEL_RED = 12
    VEL_YELLOW = 13
    VEL_BLUE = 14
    VEL_GREEN = 15

    def __init__(self, raw_packet):
        self.packet = raw_packet.hex()
        self.new_packet = {}

    def getDrums(self):
        self.new_packet.update({
            vg.XUSB_BUTTON.XUSB_GAMEPAD_B: bool(int(self.packet[self.POS_PAD], 16) & self.VAL_PAD_RED),
            vg.XUSB_BUTTON.XUSB_GAMEPAD_Y: bool(int(self.packet[self.POS_PAD], 16) & self.VAL_PAD_YELLOW),
            vg.XUSB_BUTTON.XUSB_GAMEPAD_X: bool(int(self.packet[self.POS_PAD], 16) & self.VAL_PAD_BLUE),
            vg.XUSB_BUTTON.XUSB_GAMEPAD_A: bool(int(self.packet[self.POS_PAD], 16) & self.VAL_PAD_GREEN),
            vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER: bool(int(self.packet[self.POS_PEDAL], 16) & self.VAL_PEDAL_ONE),
            vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER: bool(int(self.packet[self.POS_PEDAL], 16) & self.VAL_PEDAL_TWO),
        })
        
    def getDpad(self):
        self.new_packet.update({
            vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP: bool(int(self.packet[self.POS_DPAD], 16) & self.VAL_DPAD_UP),
            vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN: bool(int(self.packet[self.POS_DPAD], 16) & self.VAL_DPAD_DOWN),
            vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT: bool(int(self.packet[self.POS_DPAD], 16) & self.VAL_DPAD_LEFT),
            vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT: bool(int(self.packet[self.POS_DPAD], 16) & self.VAL_DPAD_RIGHT),
        })
    
    def getButtons(self):
        self.new_packet.update({
            vg.XUSB_BUTTON.XUSB_GAMEPAD_START: bool(int(self.packet[self.POS_START], 16) & self.VAL_START),
            vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK: bool(int(self.packet[self.POS_BACK], 16) & self.VAL_BACK),
            vg.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE: bool(int(self.packet[self.POS_GUIDE], 16) == self.VAL_GUIDE),
        })        

    def createDrumsPacket(self):
        self.getDrums()
        self.getDpad()
        self.getButtons()

        print(self.packet)

        return self.new_packet