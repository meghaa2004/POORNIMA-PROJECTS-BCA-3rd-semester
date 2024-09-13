import math

print("------------------------------------------------PASSWORD STRENGTH CHECKER---------------------------")

def count_character_types(input_string):
    count_digits = 0
    count_uppercase = 0
    count_lowercase = 0
    count_special = 0

    for char in input_string:
        if char.isdigit():
            count_digits += 1
        elif char.isupper():
            count_uppercase += 1
        elif char.islower():
            count_lowercase += 1
        else:
            count_special += 1

    char_set_size = 0
    if count_digits > 0:
        char_set_size += 10   
    if count_uppercase > 0:
        char_set_size += 26   
    if count_lowercase > 0:
        char_set_size += 26   
    if count_special > 0:
        char_set_size += 32   


    def combi(password):
        r = len(password)
        return char_set_size ** r

    # Function to estimate the time to crack the password
    def crack_time(no_of_combi, attempts_per_second=10000000):
        time_seconds = no_of_combi / attempts_per_second
        time_minutes = time_seconds / 60
        time_hours = time_minutes / 60
        return time_seconds, time_minutes, time_hours

    ### password length 
    if count_digits != 0 and count_uppercase == 0 and count_lowercase == 0 and count_special == 0:
        strength = "WEAK - Password only contains numbers."
    elif count_digits == 0 and count_uppercase != 0 and count_lowercase == 0 and count_special == 0:
        strength = "WEAK - Password only contains Uppercase alphabets."
    elif count_digits == 0 and count_uppercase == 0 and count_lowercase != 0 and count_special == 0:
        strength = "WEAK - Password only contains Lowercase alphabets."
    elif count_digits == 0 and count_uppercase == 0 and count_lowercase == 0 and count_special != 0:
        strength = "WEAK - Password only contains special characters."
    elif count_digits != 0 and count_uppercase != 0 and count_lowercase == 0 and count_special == 0:
        strength = "MEDIUM - Password contains Numbers and Uppercase alphabets."
    elif count_digits != 0 and count_uppercase == 0 and count_lowercase != 0 and count_special == 0:
        strength = "MEDIUM - Password contains Numbers and Lowercase alphabets."
    elif count_digits != 0 and count_uppercase == 0 and count_lowercase == 0 and count_special != 0:
        strength = "MEDIUM - Password contains Numbers and special characters."
    elif count_digits == 0 and count_uppercase != 0 and count_lowercase != 0 and count_special == 0:
        strength = "MEDIUM - Password contains Lower and Uppercase alphabets."
    elif count_digits == 0 and count_uppercase != 0 and count_lowercase == 0 and count_special != 0:
        strength = "MEDIUM - Password contains Uppercase alphabets and special characters."
    elif count_digits == 0 and count_uppercase == 0 and count_lowercase != 0 and count_special != 0:
        strength = "MEDIUM - Password contains Lowercase alphabets and special characters."
    elif count_digits != 0 and count_uppercase != 0 and count_lowercase != 0 and count_special == 0:
        strength = "STRONG - Password does not contain special characters."
    elif count_digits != 0 and count_uppercase != 0 and count_lowercase == 0 and count_special != 0:
        strength = "STRONG - Password does not contain lowercase alphabets."
    elif count_digits == 0 and count_uppercase != 0 and count_lowercase != 0 and count_special != 0:
        strength = "STRONG - Password does not contain numbers."
    else:
        strength = "VERY STRONG - Password contains all data types."

    no_of_combi = combi(input_string)
    time_seconds, time_minutes, time_hours = crack_time(no_of_combi)
    
    #### result
    print("\nPassword Analysis Results:")
    print("-" * 50)
    print(f"Password: {input_string}")
    print(f"Strength: {strength}")
    print(f"Digits: {count_digits}")
    print(f"Uppercase Letters: {count_uppercase}")
    print(f"Lowercase Letters: {count_lowercase}")
    print(f"Special Characters: {count_special}")
    print(f"Possible Combinations: {no_of_combi:,}")
    print(f"Estimated Time to Crack:")
    print(f"  Seconds: {time_seconds:,.0f}")
    print(f"  Minutes: {time_minutes:,.2f}")
    print(f"  Hours:   {time_hours:,.2f}")
    print("-" * 50)

# Input password
password = input("Enter password: ")
count_character_types(password)
