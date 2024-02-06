# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 23:27:53 2022

Tkinter GUI Code for Phidgets 64-LED Board (1032B)
University of Leicester
School of Physics and Astronomy

@author: Conan Murgatroyd
"""
import tkinter as tkr
from Phidget22.Phidget import *
from Phidget22.Devices.DigitalOutput import *

__all__ = ['LedWindow', 'led_quit']

class LedWindow:
    """
    Description:
        Defines the buttons and initialisation for a Tkinter GUI
        for a Phidgets22 1032B LED Board. Defines 64 buttons which
        control all 64 of the LED's on the board via on/off buttons.

    Params: win.
        The tkinter window in which the following button should be placed.

    Requirements:
        Requires 'phidget22.dll' to be placed in same directory as project.
    """
    def __init__(self, win):
        # Define Status of all 64 LED's as off (0 = off, 1 = on)
        self.status = [0]*64 
        
        # Create Buttons and Labels for each LED
        # LED_0
        self.label_0 = tkr.Label(win, text='LED 0')
        self.button_0 = tkr.Button(win, text='On/Off', command = lambda: self.led(0))
        # LED_1
        self.label_1 = tkr.Label(win, text='LED 1')
        self.button_1 = tkr.Button(win, text='On/Off', command = lambda:self.led(1))
        # LED_2
        self.label_2 = tkr.Label(win, text='LED 2')
        self.button_2 = tkr.Button(win, text='On/Off', command = lambda:self.led(2))
        # LED_3
        self.label_3 = tkr.Label(win, text='LED 3')
        self.button_3 = tkr.Button(win, text='On/Off', command = lambda:self.led(3))
        # LED_4
        self.label_4 = tkr.Label(win, text='LED 4')
        self.button_4 = tkr.Button(win, text='On/Off', command = lambda:self.led(4))
        # LED_5
        self.label_5 = tkr.Label(win, text='LED 5')
        self.button_5 = tkr.Button(win, text='On/Off', command = lambda:self.led(5))
        # LED_6
        self.label_6 = tkr.Label(win, text='LED 6')
        self.button_6 = tkr.Button(win, text='On/Off', command = lambda:self.led(6))
        # LED_7
        self.label_7 = tkr.Label(win, text='LED 7')
        self.button_7 = tkr.Button(win, text='On/Off', command = lambda:self.led(7))
        # LED_8
        self.label_8 = tkr.Label(win, text='LED 8')
        self.button_8 = tkr.Button(win, text='On/Off', command = lambda:self.led(8))
        # LED_9
        self.label_9 = tkr.Label(win, text='LED 9')
        self.button_9 = tkr.Button(win, text='On/Off', command = lambda:self.led(9))
        # LED_10
        self.label_10 = tkr.Label(win, text='LED 10')
        self.button_10 = tkr.Button(win, text='On/Off', command = lambda:self.led(10))
        # LED_11
        self.label_11 = tkr.Label(win, text='LED 11')
        self.button_11 = tkr.Button(win, text='On/Off', command = lambda:self.led(11))
        # LED_12
        self.label_12 = tkr.Label(win, text='LED 12')
        self.button_12 = tkr.Button(win, text='On/Off', command = lambda:self.led(12))
        # LED_13
        self.label_13 = tkr.Label(win, text='LED 13')
        self.button_13 = tkr.Button(win, text='On/Off', command = lambda:self.led(13))
        # LED_14
        self.label_14 = tkr.Label(win, text='LED 14')
        self.button_14 = tkr.Button(win, text='On/Off', command = lambda:self.led(14))
        # LED_15
        self.label_15 = tkr.Label(win, text='LED 15')
        self.button_15 = tkr.Button(win, text='On/Off', command = lambda:self.led(15))
        # LED_16
        self.label_16 = tkr.Label(win, text='LED 16')
        self.button_16 = tkr.Button(win, text='On/Off', command = lambda:self.led(16))
        # LED_17
        self.label_17 = tkr.Label(win, text='LED 17')
        self.button_17 = tkr.Button(win, text='On/Off', command = lambda:self.led(17))
        # LED_18
        self.label_18 = tkr.Label(win, text='LED 18')
        self.button_18 = tkr.Button(win, text='On/Off', command = lambda:self.led(18))
        # LED_19
        self.label_19 = tkr.Label(win, text='LED 19')
        self.button_19 = tkr.Button(win, text='On/Off', command = lambda:self.led(19))
        # LED_20
        self.label_20 = tkr.Label(win, text='LED 20')
        self.button_20 = tkr.Button(win, text='On/Off', command = lambda:self.led(20))
        # LED_21
        self.label_21 = tkr.Label(win, text='LED 21')
        self.button_21 = tkr.Button(win, text='On/Off', command = lambda:self.led(21))
        # LED_22
        self.label_22 = tkr.Label(win, text='LED 22')
        self.button_22 = tkr.Button(win, text='On/Off', command = lambda:self.led(22))
        # LED_23
        self.label_23 = tkr.Label(win, text='LED 23')
        self.button_23 = tkr.Button(win, text='On/Off', command = lambda:self.led(23))
        # LED_24
        self.label_24 = tkr.Label(win, text='LED 24')
        self.button_24 = tkr.Button(win, text='On/Off', command = lambda:self.led(24))
        # LED_25
        self.label_25 = tkr.Label(win, text='LED 25')
        self.button_25 = tkr.Button(win, text='On/Off', command = lambda:self.led(25))
        # LED_26
        self.label_26 = tkr.Label(win, text='LED 26')
        self.button_26 = tkr.Button(win, text='On/Off', command = lambda:self.led(26))
        # LED_27
        self.label_27 = tkr.Label(win, text='LED 27')
        self.button_27 = tkr.Button(win, text='On/Off', command = lambda:self.led(27))
        # LED_28
        self.label_28 = tkr.Label(win, text='LED 28')
        self.button_28 = tkr.Button(win, text='On/Off', command = lambda:self.led(28))
        # LED_29
        self.label_29 = tkr.Label(win, text='LED 29')
        self.button_29 = tkr.Button(win, text='On/Off', command = lambda:self.led(29))
        # LED_30
        self.label_30 = tkr.Label(win, text='LED 30')
        self.button_30 = tkr.Button(win, text='On/Off', command = lambda:self.led(30))
        # LED_31
        self.label_31 = tkr.Label(win, text='LED 31')
        self.button_31 = tkr.Button(win, text='On/Off', command = lambda:self.led(31))
        # LED_32
        self.label_32 = tkr.Label(win, text='LED 32')
        self.button_32 = tkr.Button(win, text='On/Off', command = lambda:self.led(32))
        # LED_33
        self.label_33 = tkr.Label(win, text='LED 33')
        self.button_33 = tkr.Button(win, text='On/Off', command = lambda:self.led(33))
        # LED_34
        self.label_34 = tkr.Label(win, text='LED 34')
        self.button_34 = tkr.Button(win, text='On/Off', command = lambda:self.led(34))
        # LED_35
        self.label_35 = tkr.Label(win, text='LED 35')
        self.button_35 = tkr.Button(win, text='On/Off', command = lambda:self.led(35))
        # LED_36
        self.label_36 = tkr.Label(win, text='LED 36')
        self.button_36 = tkr.Button(win, text='On/Off', command = lambda:self.led(36))
        # LED_37
        self.label_37 = tkr.Label(win, text='LED 37')
        self.button_37 = tkr.Button(win, text='On/Off', command = lambda:self.led(37))
        # LED_38
        self.label_38 = tkr.Label(win, text='LED 38')
        self.button_38 = tkr.Button(win, text='On/Off', command = lambda:self.led(38))
        # LED_39
        self.label_39 = tkr.Label(win, text='LED 39')
        self.button_39 = tkr.Button(win, text='On/Off', command = lambda:self.led(39))
        # LED_40
        self.label_40 = tkr.Label(win, text='LED 40')
        self.button_40 = tkr.Button(win, text='On/Off', command = lambda:self.led(40))
        # LED_41
        self.label_41 = tkr.Label(win, text='LED 41')
        self.button_41 = tkr.Button(win, text='On/Off', command = lambda:self.led(41))
        # LED_42
        self.label_42 = tkr.Label(win, text='LED 42')
        self.button_42 = tkr.Button(win, text='On/Off', command = lambda:self.led(42))
        # LED_43
        self.label_43 = tkr.Label(win, text='LED 43')
        self.button_43 = tkr.Button(win, text='On/Off', command = lambda:self.led(43))
        # LED_44
        self.label_44 = tkr.Label(win, text='LED 44')
        self.button_44 = tkr.Button(win, text='On/Off', command = lambda:self.led(44))
        # LED_45
        self.label_45 = tkr.Label(win, text='LED 45')
        self.button_45 = tkr.Button(win, text='On/Off', command = lambda:self.led(45))
        # LED_46
        self.label_46 = tkr.Label(win, text='LED 46')
        self.button_46 = tkr.Button(win, text='On/Off', command = lambda:self.led(46))
        # LED_47
        self.label_47 = tkr.Label(win, text='LED 47')
        self.button_47 = tkr.Button(win, text='On/Off', command = lambda:self.led(47))
        # LED_48
        self.label_48 = tkr.Label(win, text='LED 48')
        self.button_48 = tkr.Button(win, text='On/Off', command = lambda:self.led(48))
        # LED_49
        self.label_49 = tkr.Label(win, text='LED 49')
        self.button_49 = tkr.Button(win, text='On/Off', command = lambda:self.led(49))
        # LED_50
        self.label_50 = tkr.Label(win, text='LED 50')
        self.button_50 = tkr.Button(win, text='On/Off', command = lambda:self.led(50))
        # LED_51
        self.label_51 = tkr.Label(win, text='LED 51')
        self.button_51 = tkr.Button(win, text='On/Off', command = lambda:self.led(51))
        # LED_52
        self.label_52 = tkr.Label(win, text='LED 52')
        self.button_52 = tkr.Button(win, text='On/Off', command = lambda:self.led(52))
        # LED_53
        self.label_53 = tkr.Label(win, text='LED 53')
        self.button_53 = tkr.Button(win, text='On/Off', command = lambda:self.led(53))
        # LED_54
        self.label_54 = tkr.Label(win, text='LED 54')
        self.button_54 = tkr.Button(win, text='On/Off', command = lambda:self.led(54))
        # LED_55
        self.label_55 = tkr.Label(win, text='LED 55')
        self.button_55 = tkr.Button(win, text='On/Off', command = lambda:self.led(55))
        # LED_56
        self.label_56 = tkr.Label(win, text='LED 56')
        self.button_56 = tkr.Button(win, text='On/Off', command = lambda:self.led(56))
        # LED_57
        self.label_57 = tkr.Label(win, text='LED 57')
        self.button_57 = tkr.Button(win, text='On/Off', command = lambda:self.led(57))
        # LED_58
        self.label_58 = tkr.Label(win, text='LED 58')
        self.button_58 = tkr.Button(win, text='On/Off', command = lambda:self.led(58))
        # LED_59
        self.label_59 = tkr.Label(win, text='LED 59')
        self.button_59 = tkr.Button(win, text='On/Off', command = lambda:self.led(59))
        # LED60
        self.label_60 = tkr.Label(win, text='LED 60')
        self.button_60 = tkr.Button(win, text='On/Off', command = lambda:self.led(60))
        # LED_61
        self.label_61 = tkr.Label(win, text='LED 61')
        self.button_61 = tkr.Button(win, text='On/Off', command = lambda:self.led(61))
        # LED_62
        self.label_62 = tkr.Label(win, text='LED 62')
        self.button_62 = tkr.Button(win, text='On/Off', command = lambda:self.led(62))
        # LED_63
        self.label_63 = tkr.Label(win, text='LED 63')
        self.button_63 = tkr.Button(win, text='On/Off', command = lambda:self.led(63))
        
        # Create a variable containing all labels so we can place them in a grid
        self.lab = [
            self.label_0, self.label_1, self.label_2, self.label_3,
            self.label_4, self.label_5, self.label_6, self.label_7,
            self.label_8, self.label_9, self.label_10, self.label_11,
            self.label_12, self.label_13, self.label_14, self.label_15,
            self.label_16, self.label_17, self.label_18, self.label_19,
            self.label_20, self.label_21, self.label_22, self.label_23,
            self.label_24, self.label_25, self.label_26, self.label_27,
            self.label_28, self.label_29, self.label_30, self.label_31,
            self.label_32, self.label_33, self.label_34, self.label_35,
            self.label_36, self.label_37, self.label_38, self.label_39,
            self.label_40, self.label_41, self.label_42, self.label_43,
            self.label_44, self.label_45, self.label_46, self.label_47,
            self.label_48, self.label_49, self.label_50, self.label_51,
            self.label_52, self.label_53, self.label_54, self.label_55,
            self.label_56, self.label_57, self.label_58, self.label_59,
            self.label_60, self.label_61, self.label_62, self.label_63
            ]
        # Create a variable containing all buttons so we can place them in a grid
        self.but = [
            self.button_0, self.button_1, self.button_2, self.button_3,
            self.button_4, self.button_5, self.button_6, self.button_7,
            self.button_8, self.button_9, self.button_10, self.button_11,
            self.button_12, self.button_13, self.button_14, self.button_15,
            self.button_16, self.button_17, self.button_18, self.button_19,
            self.button_20, self.button_21, self.button_22, self.button_23,
            self.button_24, self.button_25, self.button_26, self.button_27,
            self.button_28, self.button_29, self.button_30, self.button_31,
            self.button_32, self.button_33, self.button_34, self.button_35,
            self.button_36, self.button_37, self.button_38, self.button_39,
            self.button_40, self.button_41, self.button_42, self.button_43,
            self.button_44, self.button_45, self.button_46, self.button_47,
            self.button_48, self.button_49, self.button_50, self.button_51,
            self.button_52, self.button_53, self.button_54, self.button_55,
            self.button_56, self.button_57, self.button_58, self.button_59,
            self.button_60, self.button_61, self.button_62, self.button_63
            ]
        
        # Create 8 x 16 grid to separate 64 LED's into 4 regions of 16 rows
        # with 8 columns for the labels and buttons (hence 2 columns per LED and
        # therefore 8 columns in total)
        count = 0
        for j in range(4):
            for i in range(16):
                self.lab[count].grid(row=i,column=2*j, padx=20, pady=5)
                self.but[count].grid(row=i,column=2*j+1)
                count += 1
                
        # Create an instance of DigitalOutput class for each LED from Phidgets Package 
        # for each LED.
        self.digital_output_0 = DigitalOutput()
        self.digital_output_1 = DigitalOutput()
        self.digital_output_2 = DigitalOutput()
        self.digital_output_3 = DigitalOutput()
        self.digital_output_4 = DigitalOutput()
        self.digital_output_5 = DigitalOutput()
        self.digital_output_6 = DigitalOutput()
        self.digital_output_7 = DigitalOutput()
        self.digital_output_8 = DigitalOutput()
        self.digital_output_9 = DigitalOutput()
        self.digital_output_10 = DigitalOutput()
        self.digital_output_11 = DigitalOutput()
        self.digital_output_12 = DigitalOutput()
        self.digital_output_13 = DigitalOutput()
        self.digital_output_14 = DigitalOutput()
        self.digital_output_15 = DigitalOutput()
        self.digital_output_16 = DigitalOutput()
        self.digital_output_17 = DigitalOutput()
        self.digital_output_18 = DigitalOutput()
        self.digital_output_19 = DigitalOutput()
        self.digital_output_20 = DigitalOutput()
        self.digital_output_21 = DigitalOutput()
        self.digital_output_22 = DigitalOutput()
        self.digital_output_23 = DigitalOutput()
        self.digital_output_24 = DigitalOutput()
        self.digital_output_25 = DigitalOutput()
        self.digital_output_26 = DigitalOutput()
        self.digital_output_27 = DigitalOutput()
        self.digital_output_28 = DigitalOutput()
        self.digital_output_29 = DigitalOutput()
        self.digital_output_30 = DigitalOutput()
        self.digital_output_31 = DigitalOutput()
        self.digital_output_32 = DigitalOutput()
        self.digital_output_33 = DigitalOutput()
        self.digital_output_34 = DigitalOutput()
        self.digital_output_35 = DigitalOutput()
        self.digital_output_36 = DigitalOutput()
        self.digital_output_37 = DigitalOutput()
        self.digital_output_38 = DigitalOutput()
        self.digital_output_39 = DigitalOutput()
        self.digital_output_40 = DigitalOutput()
        self.digital_output_41 = DigitalOutput()
        self.digital_output_42 = DigitalOutput()
        self.digital_output_43 = DigitalOutput()
        self.digital_output_44 = DigitalOutput()
        self.digital_output_45 = DigitalOutput()
        self.digital_output_46 = DigitalOutput()
        self.digital_output_47 = DigitalOutput()
        self.digital_output_48 = DigitalOutput()
        self.digital_output_49 = DigitalOutput()
        self.digital_output_50 = DigitalOutput()
        self.digital_output_51 = DigitalOutput()
        self.digital_output_52 = DigitalOutput()
        self.digital_output_53 = DigitalOutput()
        self.digital_output_54 = DigitalOutput()
        self.digital_output_55 = DigitalOutput()
        self.digital_output_56 = DigitalOutput()
        self.digital_output_57 = DigitalOutput()
        self.digital_output_58 = DigitalOutput()
        self.digital_output_59 = DigitalOutput()
        self.digital_output_60 = DigitalOutput()
        self.digital_output_61 = DigitalOutput()
        self.digital_output_62 = DigitalOutput()
        self.digital_output_63 = DigitalOutput()
        
        # Create a list for all the variables for each LED port so that
        # x[0] specifies digital_output_0,  x[1] specifies digital_output_1 etc.
        self.led_status =[
            self.digital_output_0, self.digital_output_1,
            self.digital_output_2, self.digital_output_3,
            self.digital_output_4, self.digital_output_5,
            self.digital_output_6, self.digital_output_7,
            self.digital_output_8, self.digital_output_9,
            self.digital_output_10, self.digital_output_11,
            self.digital_output_12, self.digital_output_13,
            self.digital_output_14, self.digital_output_15,
            self.digital_output_16, self.digital_output_17,
            self.digital_output_18, self.digital_output_19,
            self.digital_output_20, self.digital_output_21,
            self.digital_output_22, self.digital_output_23,
            self.digital_output_24, self.digital_output_25,
            self.digital_output_26, self.digital_output_27,
            self.digital_output_28, self.digital_output_29,
            self.digital_output_30, self.digital_output_31,
            self.digital_output_32, self.digital_output_33,
            self.digital_output_34, self.digital_output_35,
            self.digital_output_36, self.digital_output_37,
            self.digital_output_38, self.digital_output_39,
            self.digital_output_40, self.digital_output_41,
            self.digital_output_42, self.digital_output_43,
            self.digital_output_44, self.digital_output_45,
            self.digital_output_46, self.digital_output_47,
            self.digital_output_48, self.digital_output_49,
            self.digital_output_50, self.digital_output_51,
            self.digital_output_52, self.digital_output_53,
            self.digital_output_54, self.digital_output_55,
            self.digital_output_56, self.digital_output_57,
            self.digital_output_58, self.digital_output_59,
            self.digital_output_60, self.digital_output_61,
            self.digital_output_62, self.digital_output_63]


    def led(self, val):
        """
        Description:
            When function is run, it will cycle a specific LED into its
            opposite state - e.g., from on to off or vica versa. The LED
            is specified using the 'val' parameter.

        Params: val.
            The integer value of 'val' selects which of the 64 LED's to turn on or off.
        """
        # Set the channel to the correct LED - e.g. digital_output_63.setchannel(63)
        self.led_status[val].setChannel(val)
        
        # Check the status of the LED.
        if self.status[val] == 0: # If status is off turn LED on.
            self.led_status[val].openWaitForAttachment(5000)
            self.led_status[val].setDutyCycle(1)
            self.status[val] = 1
            
        else: # If status is on, turn LED off.
            self.led_status[val].close()
            self.status[val] = 0


def led_quit(led_win):
    """
    Description:
        When function is run, it will cycle all 64 LED's on Phidgets
        board to off so board can be powered down safely.

    Params: led_win.
        Specifies the LedWindow Class which contains the variables.

    E.g.
        <<< import tkinter as tkr
        <<< led_window = tkr.Toplevel()
        <<< led_win = LedWindow(led_window)
        <<< led_quit(led_win)
        
    """
    for i in range(64):
        led_win.led_status[i].close()
