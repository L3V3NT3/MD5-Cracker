import hashlib
import os
import sys
import time
import md5

upper_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_letter = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"

def five_lower():
    counter = 0
    
    hash_submitted = raw_input("MD5 Hash >>> ")
    hash_object_MD5 = str(hash_submitted)
    confirm = raw_input(str(hash_object_MD5) + " ==> Hash. Continue? (Y / N): ")
    if confirm == "Y":
        pass
    else:
        time.sleep(1)
        quit()
   
    for a in lower_letter:
        for b in lower_letter:
            for c in lower_letter:
                for d in lower_letter:
                    for e in lower_letter:
                        counter = counter + 1
                        password = a + b + c + d + e
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
                            print("[ATTEMPT - " + str(counter) + "] " + a + b + c + d + e)
                                            

five_lower()
