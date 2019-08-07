#!/usr/bin/env python

import usb
import struct
import time
import warnings

# MPUSBRead/Write functions, 3-byte packet: control byte, data_low, data_high
SET_ACCURACY = 0x01
SET_RETRACT_LIMIT = 0x02
SET_EXTEND_LIMIT = 0x03
SET_MOVEMENT_THRESHOLD = 0x04
SET_STALL_TIME = 0x05
SET_PWM_THRESHOLD = 0x06
SET_DERIVATIVE_THRESHOLD = 0x07
SET_DERIVATIVE_MAXIMUM = 0x08
SET_DERIVATIVE_MINIMUM = 0x09
SET_PWM_MAXIMUM = 0x0A
SET_PWM_MINIMUM = 0x0B
SET_PROPORTIONAL_GAIN = 0x0C
SET_DERIVATIVE_GAIN = 0x0D
SET_AVERAGE_RC = 0x0E
SET_AVERAGE_ADC = 0x0F

GET_FEEDBACK = 0x10
SET_POSITION = 0x20
SET_SPEED = 0x21
DISABLE_MANUAL = 0x30
RESET = 0xFF


# def raise_if_out_of_bounds(data):
#     if data < 0 or 1023 < data:
#         raise ValueError('data out of bounds, command not send')


class Lac(object):

    def __init__(self):
        self.dev = usb.core.find(idVendor=0x04d8, idProduct=0xfc5f)
	self.dev.reset()
        self.dev.set_configuration()

    # def set_accuracy(self, request):
    #     if check_bounds(request):
    #         return self.write(SET_ACCURACY, request)


    # def set_retract_limit(self, request):
    #     if check_bounds(request):
    #         return self.write(SET_RETRACT_LIMIT, request)


    # def set_extend_limit(self, request):
    #     if check_bounds(request):
    #         return self.write(SET_EXTEND_LIMIT, request)


    def get_feedback(self):
        return self.write(GET_FEEDBACK)


    def set_position(self, request):
        # if check_bounds(request):
        return self.write(SET_POSITION, request)


    def set_speed(self, request):
        # if check_bounds(request):
        return self.write(SET_SPEED, request)


    def reset(self):
        return self.write(RESET)


    def write(self, command, request=0):
        hi_byte=(request//256)&255
        lo_byte=request&255
        message=struct.pack(b'BBB', command, lo_byte, hi_byte)
        self.dev.write(1, message, 100)
        time.sleep(0.05)
        response=self.dev.read(0x81,3,100)
        time.sleep(0.05)
        return response[2]*256+response[1]




    #TODO: Figure out how to stop the actuator after a command has been sent
    #def stop(self):
    #    send_reset()


