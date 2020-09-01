# -*- coding: utf-8 -*-
import hashlib
import os
import sys
import time
import md5

##########################################################################################################################3
#############################################################################################################################################################################################
def help_exc():
    print (""" - format (list formats)
 - format <parameter>
 - info
 - exit
 - clear""")
    start_commands()
#############################################################################################################################################################################################
def format_exc():
    print("""/!-- Dictionary Attacks --!\

(A) WORDLIST (ENGLISH)

/!-- Bruteforce Attacks --!\

* ~ 4 DIGITS *
(B) 4 LOWER
(C) 4 UPPER
(D) 1 UPPER, 3 LOWER

* ~ 5 DIGITS *
(E) 5 LOWER
(F) 5 UPPER
(G) 1 UPPER, 4 LOWER
(H) 1 UPPER, 4 LOWER, 1 NUMBER
(I) 1 UPPER, 4 LOWER, 2 NUMBER
(J) 1 UPPER, 4 LOWER, 3 NUMBER

* ~ 6 DIGITS *
(K) 6 LOWER
(L) 6 UPPER
(M) 1 UPPER, 5 LOWER
(N) 1 UPPER, 5 LOWER, 1 NUMBER
(O) 1 UPPER, 5 LOWER, 2 NUMBER
(P) 1 UPPER, 5 LOWER, 3 NUMBER

According to a recent study, most of the passwords (61%) were right at the password limit, either 8 or 9 characters long. The average length was 9.6 characters, and the average password consisted of 1.1 upper-case letters, 6.1 lower-case letters, 2.2 numbers and 0.2 special characters. I used this info to create an average scan which will satisfy your day to day needs when cracking MD5 hashes. 

* AVERAGE SCAN *
(Q) BASIC AVERAGE SCAN - 1 UPPER, 6 LOWER, 2 NUMBER
(R) INTESIVE AVERAGE SCAN - 1 UPPER, 6 LOWER, 2 NUMBER, 1 SPECIAL CHARACTER
""")
    start_commands()
############################################################################################################################################################################################
def info_exc():
    print("""MD5 Hash Cracker created by L3V3NT3. This python script provides
a command-line based interface, with loads of options
for different formats. It uses a bruteforcing method
in order to try every possible password. """)
    start_commands()
#############################################################################################################################################################################################
def clear_exc():
    try:
        os.system("clear")
    except:
        try:
            os.system("cls")
        except:
            pass
#############################################################################################################################################################################################
def one_upper_six_lower():
    counter = 0
    question = raw_input("Enter MD5 Hash or Convert Password to MD5 Hash (1 / 2): ")
    
    if question == "1":
        hash_submitted = raw_input("MD5 Hash >>> ")
        hash_object_MD5 = str(hash_submitted)
        confirm = raw_input(str(hash_object_MD5) + " ==> Hash. Continue? (Y / N): ")
        if confirm == "Y":
            pass
        else:
            time.sleep(1)
            quit()
    elif question == "2":
        hash_object = raw_input("Password >>> ")
        if len(hash_object) < 7 or len(hash_object) > 7:
            print("Wrong Format! Invalid Password Lenght: "+str(len(hash_object)) + ". Select other format!")
            print("Quitting...")
            quit()
        else:
            pass
        hash_object = hashlib. md5(str(hash_object).encode())
        hash_object_MD5 = hash_object.hexdigest()
        confirm = raw_input(str(hash_object_MD5) + " ==> Hash. Continue? (Y / N): ")
        if confirm == "Y":
            pass
        else:
            print("Quitting...")
            time.sleep(1)
            quit()
            
    for first_letter in upper_letter:
        for a in lower_letter:
            for b in lower_letter:
                for c in lower_letter:
                    for d in lower_letter:
                        for e in lower_letter:
                            for f in lower_letter:
                                    counter = counter + 1
                                    password = first_letter + a + b + c + d + e + f
                                    attempt_hash = hashlib.md5(password.encode())
                                    attempt_hash_MD5 = attempt_hash.hexdigest()
                                    
                                    if attempt_hash_MD5 == hash_object_MD5:
                                        print("[CORRECT] "+ password)
                                        print("-" * 50)
                                        print("Number of Attempts: "+ str(counter))
                                        print("Password is "+ password)
                                        
                                        if counter >= 20000000:
                                            print("Strenght: A")
                                        elif counter <= 2000000 and counter > 200000:
                                            print("Strenght: B")
                                        elif counter <= 200000 and counter > 20000:
                                            print("Strenght: C")
                                        elif counter <= 20000 and counter > 2000:
                                            print("Strenght: D")
                                        elif counter <= 2000 and counter > 200:
                                            print("Strenght: E")
                                        elif counter <= 200:
                                            print("Strenght: F")

                                        print("-" * 50)


                                        restart = raw_input("Continue? (Y / N): ")
                                        if restart == "Y":
                                            python = sys.executable
                                            os.execl(python, python, *sys.argv)
                                        else:
                                            quit()
                                        
                                        
                                    else:
                                        print("[ATTEMPT - " + str(counter) + "] " + first_letter + a + b + c + d + e + f)
                                
#############################################################################################################################################################################################
def nl():
    print("""   """)
#############################################################################################################################################################################################

logo = """

__________________________s$______________s
_________________________.s$$_____________s$
________________________s$$$’____________s$$
______________________.s$$$³´_______,___s$$³
_____________________s$$$$³______.s$’___$$³
________________,____$$$$$.______s$³____³$
________________$___$$$$$$s_____s$³_____³,
_______________s$___‘³$$$$$$s___$$$
_______________$$____³$$$$$$s.__³$$s
_______________³$.____³$$$$$$$s_.s$$$____s´
_______________`$$.____³$$$$$$$_$$$$___s³
________________³$$s____³$$$$$$s$$$³__s$’
_________________³$$s____$$$$$s$$$$’__s$$
_____________`s.__$$$$___s$$$$$$$$³_.s$$³__s
______________$$_s$$$$..s$$$$$$$$$$$$$$³__s$
______________s$.s$$$$s$$$$$$$$$$$$$$$$_s$$
_____________s$$$$$$$$$$$$$$$$$$$$$$$$$$$³
____________s$$$ssss$$$$$$$$$$$$$ssss$$$$$´
___________$$s§§§§§§§§§s$$$$$$s§§§§§§§§s$,
___________³§§§§§§§§§§§§§s$s§§§§§§§§§§§§s
___________§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§
___________³§§§§§§§§§§§§§§§§§§§§§§§§§§§§§
____________³§§§§§§§§§§§§§§§§§§§§§§§§§§§³
_____________³§§§§§§§§§§§§§§§§§§§§§§§§§³
______________³§§§§§§§§§§§§§§§§§§§§§§§³
________________³§§§§§§§§§§§§§§§§§§§³
__________________³§§§§§§§§§§§§§§§³
____________________³§§§§§§§§§§§³
_______________________³§§§§§³
_________________________³§³

             MD5 Hash Cracker by L3V3NT3
"""
#############################################################################################################################################################################################
def startup():
    try:
        os.system("clear")
    except:
        try:
            os.system("cls")
        except:
            pass
    
    print(logo)
    nl()
    print("Type 'help!' to display commands.")
    try:
        f = open("data/config.txt", "r")
        line = f.readlines()
        if line == "installed":
            f.close()
            pass
    except:
        print("Installing required elements:")
        nl()
        os.system("pip install termcolor && pip install colorama && pip install hashid")
        os.system("echo 'installed' > data/config.txt")
        
        try:
        	os.system("clear")
    	except:
        	try:
            		os.system("cls")
        	except:
            		pass
	print(logo)
    	nl()
    	print("Type 'help!' to display commands.")
	nl()
        
#############################################################################################################################################################################################
def start_commands():
    password_format = raw_input(colored('user@hashcracker: ', 'red'))

    if password_format == "":
        start_commands()

    elif password_format == "help!":
        help_exc()

    elif password_format == "format":
        format_exc()
    
    elif password_format == "format A":
        print("Format ==> (A) WORDLIST")
        wordlist_scan()

    elif password_format == "format B":
        print("Format ==> (B) 4 LOWER")
        four_lower()

    elif password_format == "format C":
        print("Format ==> (C) 4 UPPER")
        four_upper()

    elif password_format == "format D":
        print("Format ==> (D) 1 UPPER, 3 LOWER")
        one_upper_three_lower()

    elif password_format == "format E":
        print("Format ==> (E) 5 LOWER")
        five_lower()

    elif password_format == "format F":
        print("Format ==> (F) 5 UPPER")
        five_upper()

    elif password_format == "format G":
        print("Format ==> (G) 1 UPPER, 4 LOWER")
        one_upper_four_lower()

    elif password_format == "format H":
        print("Format ==> (H) 1 UPPER, 4 LOWER, 1 NUMBER")
        one_upper_four_lower_one_digit()

    elif password_format == "format I":
        print("Format ==> (I) 1 UPPER, 4 LOWER, 2 NUMBER")
        one_upper_four_lower_two_digit()

    elif password_format == "format J":
        print("Format ==> (J) 1 UPPER, 4 LOWER, 3 NUMBER")
        one_upper_four_lower_three_digit()

    elif password_format == "format K":
        print("Format ==> (K) 6 LOWER")
        six_lower()

    elif password_format == "format L":
        print("Format ==> (L) 6 UPPER")
        six_upper()
        
    elif password_format == "format M":
    	print("Format ==> (M) 1 UPPER, 5 LOWER")
    	one_upper_five_lower()
    	
    elif password_format == "format N":
    	print("Format ==> (M) 1 UPPER, 5 LOWER, 1 NUMBER")
    	one_upper_five_lower_one_digit()
    
    elif password_format == "format O":
    	print("Format ==> 1 UPPER, 5 LOWER, 2 NUMBER")
    	one_upper_five_lower_two_digit()
    
    elif password_format == "format P":
    	print("Format ==> 1 UPPER, 5 LOWER, 3 NUMBER")
    	one_upper_five_lower_three_digit()
    
    elif password_format == "format Q":
    	print("Format ==> BASIC AVERAGE SCAN")
    	basic_scan()
    	
    elif password_format == "format R":
    	print("Format ==> INTENSIVE AVERAGE SCAN")
    	int_scan()
    
    elif password_format == "info":
        info_exc()

    elif password_format == "exit":
        print("\n")
        quit()

    elif password_format == "clear":
        clear_exc()
        startup()
        start_commands()

    else:
        print("-hashcracker: "+ str(password_format) +": command not found")
        start_commands()
#############################################################################################################################################################################################
def one_upper_six_lower_one_digit():
    counter = 0
    question = raw_input("Enter MD5 Hash or Convert Password to MD5 Hash (1 / 2): ")
    
    if question == "1":
        hash_submitted = raw_input("MD5 Hash >>> ")
        hash_object_MD5 = str(hash_submitted)
        confirm = raw_input(str(hash_object_MD5) + " ==> Hash. Continue? (Y / N): ")
        if confirm == "Y":
            pass
        else:
            time.sleep(1)
            quit()
    elif question == "2":
        hash_object = raw_input("Password >>> ")
        if len(hash_object) < 8 or len(hash_object) > 8:
            print("Wrong Format! Invalid Password Lenght: "+str(len(hash_object)) + ". Select other format!")
            print("Quitting...")
            quit()
        else:
            pass
        hash_object = hashlib. md5(str(hash_object).encode())
        hash_object_MD5 = hash_object.hexdigest()
        confirm = raw_input(str(hash_object_MD5) + " ==> Hash. Continue? (Y / N): ")
        if confirm == "Y":
            pass
        else:
            print("Quitting...")
            time.sleep(1)
            quit()
            
    for first_letter in upper_letter:
        for a in lower_letter:
            for b in lower_letter:
                for c in lower_letter:
                    for d in lower_letter:
                        for e in lower_letter:
                            for f in lower_letter:
                                for g in digits:
                                    counter = counter + 1
                                    password = first_letter + a + b + c + d + e + f + g
                                    attempt_hash = hashlib.md5(password.encode())
                                    attempt_hash_MD5 = attempt_hash.hexdigest()
                                    
                                    if attempt_hash_MD5 == hash_object_MD5:
                                        print("[CORRECT] "+ password)
                                        print("-" * 50)
                                        print("Number of Attempts: "+ str(counter))
                                        print("Password is "+ password)
                                        
                                        if counter >= 20000000:
                                            print("Strenght: A")
                                        elif counter <= 2000000 and counter > 200000:
                                            print("Strenght: B")
                                        elif counter <= 200000 and counter > 20000:
                                            print("Strenght: C")
                                        elif counter <= 20000 and counter > 2000:
                                            print("Strenght: D")
                                        elif counter <= 2000 and counter > 200:
                                            print("Strenght: E")
                                        elif counter <= 200:
                                            print("Strenght: F")

                                        print("-" * 50)


                                        restart = raw_input("Continue? (Y / N): ")
                                        if restart == "Y":
                                            python = sys.executable
                                            os.execl(python, python, *sys.argv)
                                        else:
                                            quit()
             
                                    else:
                                        print("[ATTEMPT - " + str(counter) + "] " + first_letter + a + b + c + d + e + f + g)
                                        


#############################################################################################################################################################################################
def one_upper_six_lower_two_digit():
    counter = 0
    question = raw_input("Enter MD5 Hash or Convert Password to MD5 Hash (1 / 2): ")
    
    if question == "1":
        hash_submitted = raw_input("MD5 Hash >>> ")
        hash_object_MD5 = str(hash_submitted)
        confirm = raw_input(str(hash_object_MD5) + " ==> Hash. Continue? (Y / N): ")
        if confirm == "Y":
            pass
        else:
            time.sleep(1)
            quit()
    elif question == "2":
        hash_object = raw_input("Password >>> ")
        if len(hash_object) < 9 or len(hash_object) > 9:
            print("Wrong Format! Invalid Password Lenght: "+str(len(hash_object)) + ". Select other format!")
            print("Quitting...")
            quit()
        else:
            pass
        hash_object = hashlib. md5(str(hash_object).encode())
        hash_object_MD5 = hash_object.hexdigest()
        confirm = raw_input(str(hash_object_MD5) + " ==> Hash. Continue? (Y / N): ")
        if confirm == "Y":
            pass
        else:
            print("Quitting...")
            time.sleep(1)
            quit()
       
    for first_letter in upper_letter:
        for a in lower_letter:
            for b in lower_letter:
                for c in lower_letter:
                    for d in lower_letter:
                        for e in lower_letter:
                            for f in lower_letter:
                                for g in digits:
                                    for h in digits:
                                        counter = counter + 1
                                        password = first_letter + a + b + c + d + e + f + g + h
                                        attempt_hash = hashlib.md5(password.encode())
                                        attempt_hash_MD5 = attempt_hash.hexdigest()
                                        
                                        if attempt_hash_MD5 == hash_object_MD5:
                                            print("[CORRECT] "+ password)
                                            print("-" * 50)
                                            print("Number of Attempts: "+ str(counter))
                                            print("Password is "+ password)
                                            
                                            if counter >= 20000000:
                                                print("Strenght: A")
                                            elif counter <= 2000000 and counter > 200000:
                                                print("Strenght: B")
                                            elif counter <= 200000 and counter > 20000:
                                                print("Strenght: C")
                                            elif counter <= 20000 and counter > 2000:
                                                print("Strenght: D")
                                            elif counter <= 2000 and counter > 200:
                                                print("Strenght: E")
                                            elif counter <= 200:
                                                print("Strenght: F")

                                            print("-" * 50)
                                            
                                            restart = raw_input("Continue? (Y / N): ")
                                            if restart == "Y":
                                                os.system("python L3V3NT3.py")
                                                quit()
                                            else:
                                                quit()
                                            
                                        else:
                                            print("[ATTEMPT - " + str(counter) + "] " + first_letter + a + b + c + d + e + f + g + h)



#############################################################################################################################################################################################
def wordlist_scan():
    os.system("python data/wordlist.py")
#############################################################################################################################################################################################
def four_lower():
    os.system("python data/four_lower.py")
#############################################################################################################################################################################################
def four_upper():
    os.system("python data/four_upper.py")
#############################################################################################################################################################################################
def one_upper_three_lower():
    os.system("python data/one_upper_three_lower.py")
#############################################################################################################################################################################################
def five_lower():
    os.system("python data/five_lower.py")
#############################################################################################################################################################################################
def five_upper():
    os.system("python data/five_upper.py")
#############################################################################################################################################################################################
def one_upper_four_lower():
    os.system("python data/one_upper_four_lower.py")
#############################################################################################################################################################################################
def one_upper_four_lower_one_digit():
    os.system("python data/one_upper_four_lower_one_digit.py")
#############################################################################################################################################################################################
def one_upper_four_lower_two_digit():
    os.system("python data/one_upper_four_lower_two_digit.py")
#############################################################################################################################################################################################
def one_upper_four_lower_three_digit():
    os.system("python data/one_upper_four_lower_three_digit.py")
#############################################################################################################################################################################################
def six_lower():
    os.system("python data/six_lower.py")
#############################################################################################################################################################################################
def six_upper():
    os.system("python data/six_upper.py")
#############################################################################################################################################################################################
def one_upper_five_lower():
    os.system("python data/one_upper_five_lower.py")
#############################################################################################################################################################################################
def one_upper_five_lower_one_digit():
    os.system("python data/one_upper_five_lower_one_digit.py")
#############################################################################################################################################################################################
def one_upper_five_lower_two_digit():
    os.system("python data/one_upper_five_lower_two_digit.py")
#############################################################################################################################################################################################
def one_upper_five_lower_three_digit():
    os.system("python data/one_upper_five_lower_three_digit.py")
##########################################################################################################################################################################################
def basic_scan():
    os.system("python data/basic_scan.py")
####################################################################################################################################################################################
def int_scan():
    os.system("python data/int_scan.py")
####################################################################################################################################################################################

####################################################################################################################################################################################

####################################################################################################################################################################################

####################################################################################################################################################################################

startup()
upper_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_letter = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"

from colorama import init 
from termcolor import colored 
init()
        
start_commands()
