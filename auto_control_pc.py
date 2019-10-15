# -*- coding: utf-8 -*-
"""
Tự động đăng nhâp facebook trên desktop

"""
import time
import pyautogui

def controller(sdt, password): 
    # english keyboard
    #----------------------------Chrome
    # chrome icon
    pyautogui.moveTo(101, 163, duration=0.25)
    pyautogui.doubleClick()
    time.sleep(1)
    
    # ô tìm kiếm trong chrome
    pyautogui.moveTo(431, 51, duration=0.25)
    pyautogui.click()
    time.sleep(1)
    
    # nhập tìm
    pyautogui.typewrite('https', interval=0.25)
    pyautogui.hotkey('shift',';')
    pyautogui.typewrite('//www.facebook.com', interval=0.25)
    pyautogui.press('enter')
    time.sleep(1)
    
    #------------------------- facebook
    # ô nhập số điện thoại                                                           
    pyautogui.moveTo(974, 116, duration=0.25)
    pyautogui.click()
    time.sleep(1)
    
    # nhập sđt
    pyautogui.hotkey('ctrl','a')
    pyautogui.press('backspace')
    pyautogui.typewrite(sdt, interval=0.25)
    time.sleep(1)
    
    # ô nhập mk
    pyautogui.moveTo(1103, 115, duration=0.25)
    pyautogui.click()
    time.sleep(1)
    
    
    # nhập mk
    pyautogui.hotkey('ctrl','a')
    pyautogui.press('backspace')
    pyautogui.typewrite(password, interval=0.25)
    time.sleep(1)
    
    # ô đăng nhập
    pyautogui.moveTo(1237, 111)
    pyautogui.doubleClick()
    time.sleep(3)
    
    # cuộn chuột liên tục
    pyautogui.moveTo(1237, 357, duration=0.25)
    while True:
        pyautogui.scroll(-200)
        time.sleep(2)

if __name__=='__main__':
    sdt = str(input('what is your phone on facebook: '))
    password = str(input('what is ur password: '))
    print ('please set english keyboard for controlling')
    controller(sdt, password)
