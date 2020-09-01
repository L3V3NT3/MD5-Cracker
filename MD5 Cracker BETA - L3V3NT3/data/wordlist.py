import hashlib
import os
import sys
import time
import md5

upper_letter = "ABCDEFGHIJKLMNOPQRS"
lower_letter = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"


def wordlist_scan():
    counter = 0
    
    hash_submitted = raw_input("MD5 Hash >>> ")
    hash_object_MD5 = str(hash_submitted)
    confirm = raw_input(str(hash_object_MD5) + " ==> Hash. Continue? (Y / N): ")
    if confirm == "Y":
        pass
    else:
        time.sleep(1)
        quit()

    password_file = raw_input("Wordlist Path: ")

    try:
        password_file = open(str(password_file), "r")
        pass
    except:
    	try:
        	password_file = open(str(password_file), "r")
        	pass
        except:
        	print("File not found! Quitting...")
        	quit()

    for password in password_file:
        counter = counter + 1
        filemd5 = md5.new(password.strip()).hexdigest()

        if hash_object_MD5 == str(filemd5):
            print("[CORRECT] "+ password)
            print("-" * 50)
            print("Number of Attempts: "+ str(counter))
            print("Password is "+ password.strip())
                    
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
            print("[ATTEMPT - " + str(counter) + "] " + password.strip())


wordlist_scan()
