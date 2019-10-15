# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 11:57:59 2019

@author: Admin

text to speech by google
"""

from gtts import gTTS 
import os


list_text = {               "nguyenam_bet": {"i":  ["iii", "í", "ì", "ỉ", "ị", "tim", "tím", "tìm", "tỉm", "tịm"],
                                             "ê":  ["ê", "ế", "ề", "ể", "ệ", "têm", "tếm", "tềm", "xểm", "tệm"],
                                             "e":  ["e", "é", "è", "ẻ", "ẹ", "leng", "léng", "lèng", "lẻng", "lẹng"],
                                             "ia": ["ia", "ía", "ìa", "ỉa", "ịa", "tai", "tái", "tìa", "tải", "tại"]},
             "nguyenam_khongbet_khongtron": {"a":  ["anh", "ánh", "ành", "ảnh", "ạnh", "a", "á", "à", "ả", "ạ"],
                                             "ă":  ["ăng", "ắng", "ằng", "ẳng", "ặng"],
                                             "ơ":  ["ơ", "ớ", "ờ", "ở", "ợ", "cơm", "cớm", "cờm", "cởm", "cợm"],
                                             "â":  ["âu", "ấu", "ầu", "ẩu", "ậu"],
                                             "ư":  ["mưng", "mứng", "mừng", "mừng", "mửng", "mựng"],
                                             "ưa": ["dưa", "dứa", "dưa", "dửa", "dựa"]},
                           "nguyenam_tron": {"ô":  ["nhôn", "nhốn", "nhồn", "nhổn", "nhộn", "ô", "ố", "ồ", "ổ", "ộ"],
                                             "oo": ["xoong"],
                                             "o":  ["xong", "xóng", "xòng", "xỏng", "xọng", "o", "ó", "ò", "ỏ", "ọ"],
                                             "u":  ["u", "ú", "ù", "ủ", "ụ", "lun", "lún", "lùn", "lủn", "lụn"],
                                             "ua": ["ua", "ủa", "ũa", "ụa", "úa", "luôn", "luốn"]},
                                   "banam": {"u":  ["qua", "quá", "cau"],
                                             "o":  ["kao"]},
                           "phuam_moi_moi": {"m":  ["màu", "min"], 
                                             "b":  ["bàu", "bin"], 
                                             "p":  ["pàu", "pin"]},
                          "phuam_moi_rang": {"v":  ["vàu", "vin"], 
                                             "ph": ["phàu", "phin"]},
                     "phuam_luoi_rangtren": {"t":  ["tàu", "tin"], 
                                             "th": ["thàu", "thin"]},
                     "phuam_luoi_rangkhit": {"x":  ["xàu", "xin"]},
                 "phuam_luoi_chanrang_vom": {"n":  ["nàu", "nin"],
                                             "đ":  ["đàu", "đin"],
                                             "l":  ["làu", "lin"]},
                      "phuam_luoicong_vom": {"r":  ["ràu", "rin"],
                                             "tr": ["tràu", "trin"], 
                                             "s":  ["sàu", "sin"]},
                       "phuam_luoibet_vom": {"d_gi":["dàu", "din"]},
                "phuam_cuongluoingoai_vom": {"kh": ["khàu", "khin"], 
                                             "g":  ["gàu", "gin"]},
                "phuam_cuongluoitrong_vom": {"ng": ["ngàu", "ngin"], 
                                             "c":  ["càu", "cin"]},
                          "phuam_thanhhau": {"h":  ["hàu", "hin"]},
                           "phuam_matluoi": {"ch": ["chàu"],
                                             "nh": ["nhin"]},
                                   "amtac": {"tac":["ăn", "ắn", "ằn", "ặn", "ẵn", "uống", "uộng"]}         }



Folders = r"C:\Users\Admin\Desktop\phoneme"
for folder in list_text:
    
    fs = os.path.join(Folders, folder)
    os.mkdir(fs)
   
    for amvi in list_text[folder]:
        f = os.path.join(fs, amvi)
        os.mkdir(f)
        
        for am in list_text[folder][amvi]:
            sound = gTTS(text=am, lang='vi', slow=False)
            sound.save(os.path.join(f, am+'.mp3'))
    
    
