class DrumsPacket:
    POS_PAD = 8
    POS_DPAD = 9
    POS_PEDAL = 10

    VAL_DPAD_UP = 1
    VAL_DPAD_DOWN = 2 
    VAL_DPAD_LEFT = 4
    VAL_DPAD_RIGHT = 8

    VAL_PAD_RED = 2
    VAL_PAD_YELLOW = 8
    VAL_PAD_BLUE = 4
    VAL_PAD_GREEN = 1

    VAL_PEDAL_ONE = 1
    VAL_PEDAL_TWO = 2
    
    VEL_RED = 12
    VEL_YELLOW = 13
    VEL_BLUE = 14
    VEL_GREEN = 15

    def __init__(self, raw_packet):
        self.packet = raw_packet.hex()
        self.createDrumsPacket()

    def getDrums(self):
        print('red') if (int(self.packet[self.POS_PAD], 16) & self.VAL_PAD_RED) else None
        print('yellow') if (int(self.packet[self.POS_PAD], 16) & self.VAL_PAD_YELLOW) else None
        print('blue') if (int(self.packet[self.POS_PAD], 16) & self.VAL_PAD_BLUE) else None
        print('green') if (int(self.packet[self.POS_PAD], 16) & self.VAL_PAD_GREEN) else None
        
        print('pedal one') if (int(self.packet[self.POS_PEDAL], 16) & self.VAL_PEDAL_ONE) else None
        print('pedal two') if (int(self.packet[self.POS_PEDAL], 16) & self.VAL_PEDAL_TWO) else None
    
    def getDpad(self):
        print('up') if (int(self.packet[self.POS_DPAD], 16) & self.VAL_DPAD_UP) else None
        print('down') if (int(self.packet[self.POS_DPAD], 16) & self.VAL_DPAD_DOWN) else None
        print('left') if (int(self.packet[self.POS_DPAD], 16) & self.VAL_DPAD_LEFT) else None
        print('right') if (int(self.packet[self.POS_DPAD], 16) & self.VAL_DPAD_RIGHT) else None

    def createDrumsPacket(self):
        drums = self.getDrums()
        dpad = self.getDpad()