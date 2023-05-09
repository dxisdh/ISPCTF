import hashlib

hashed_key = "b3d77ed0c460ef460792f07ad1e471d5fe70ac85c514e0b21b32e49d0f1b2c55"
hash_secret = 31580683746748870831459475506823890005573670692504809

def encrypt(key):
    result = hash_secret ^ key 
    return result

def hash(user_input):
    salt = "ISP_Salt"
    return hashlib.sha256(salt.encode() + user_input.encode()).hexdigest()
    
def check_input(user_input):
    hashed_user_input = hash(user_input)
    return hashed_user_input == hashed_key

def main():
    my_string = input("What is your favorite number?: ")
    # for i in range (10000000,99999999):
    #     if check_input(str(i)) == 1:
    #         print(str(i))
    if len(my_string) == 8 and check_input(my_string):
        key = int(my_string)
        result_int = encrypt(key)
        result_bytes = result_int.to_bytes((result_int.bit_length() + 7) // 8, 'big')
        flag_str = ''
        for b in result_bytes:
            flag_str += chr(b)
        print(f"ISPCTF{{{flag_str}}}\n")
    else:
        print("That number isn't right!")
# 10658203
        
if __name__ == "__main__":
    main()
