#!/usr/bin/env python
#######################################################################################
# DiFi - A Directional WiFi Tool
# Written by: James Smith (smittix)
# Twitter: @iamsmittix
# Website: https://www.smittix.co.uk
# Platform: MacOSX and Linux (coming soon)
#######################################################################################
import sys
import os
import subprocess
os.system("clear")
## Show menu ##

a = raw_input

def my_menu(a):
    print ("      ____  _ _____ _")
    print ("     |  _ \(_)  ___(_)")
    print ("     | | | | | |_  | |")
    print ("     | |_| | |  _| | |")
    print ("     |____/|_|_|   |_|")
    print ("DiFi - Directional WiFi Tool.")
    print ("       Version 0.1")
    print ("By smittix - Smittix.co.uk")
    print (30 * '-')
    print ("     M A I N - M E N U")
    print (30 * '-')
    print ("")
    print ("1. Current Signal Strength")
    print ("2. Find Access Points")
    print ("3. Exit")    
    print 
    a=input ('Please enter your selection: ')
    print
    if a == 1:
        print 'Ok.. Measuring your current WiFi signal strength'
        print
        print ("*** Press Ctrl C to stop ***")
        print
        os.system("while i=1; do /system/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I | grep CtlRSSI; sleep 0.5; done | sed 's/agrCtlRSSI/WiFi Signal Strength/'")
        a1 = raw_input('Do you want to update the results? , y or n: ')
        print
        while a1 == 'y':
            os.system("while i=1; do /system/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I | grep CtlRSSI; sleep 0.5; done | sed 's/agrCtlRSSI/WiFi Signal Strength/'")                            
    elif a == 2:
        print 'Scanning nearby access points...'
        print
        os.system("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s")
        print
        
    elif a == 3:
        print 'You have chosen to quit'
        print
        print '......Thankyou Come Again......'
        exit()
    else:
        print 'Thats not a valid option'
        print
    x = raw_input ('Would you like to perform another task? y or n: ')
    if x == 'y':
        my_menu(a)
    else:
        print '......Thankyou Come Again......'
        return

my_menu(a)
