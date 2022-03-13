import vgamepad as vg
import usb.core
import usb.backend.libusb1

from DrumsPacket import DrumsPacket


def main():
    device = usb.core.find(idVendor=0x0E6F, idProduct=0x0171)
    
    if device is None:
        raise ValueError('Could not find RB4 PDP drums for Xbox.')
    
    gamepad = vg.VX360Gamepad()

    while True:
        data = device.read(0x81, 0x40 , 3000).tobytes()
        drums = DrumsPacket(data)
        packet = drums.createDrumsPacket()

        for button, value in packet.items():
            if value == 0:
                gamepad.release_button(button=button)
            elif value > 0:
                gamepad.press_button(button=button)
            gamepad.update()

if __name__ == '__main__':
    main()