# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random
import string
import time
import hashlib

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# def quadratic_residue(p):
#     residues = []

#     for q in range(1, p):
#         for x in range(1, p):
#             if x**2 % p == q % p:
#                 residues.append(q)
#                 break

#     return residues


# openssl gendh 1024 | openssl asn1parse

p = 0xD9EC41017C7A1BA2546279AA8A4276E459C7DB9190B9FBE936FEED625EED536445749460E38F8430112E53B9FC4DA1DFF7DAD7EFBA8CB837EDD161F31A7029B5F4EC2501DD4906E3CA6483263E324A4E70390449BCF2682D210AE3EA6CF69F400835BD3B6C256CA3EC37A4992C7421432214FDAA759FE09A07052AC6E6FCFB6B
q = 0xF0A571413BC4066D616194679CE19486B5DB930A1C8F8C4F11F13BC829EB44F1803E6C8BA160044FA64F85ADF171D8C6B8304F36DBD3D063FA83212DF0C7353BE8B220CF437F2EF092CE040A1F1CD02E0DB2C8979E82838B4A9A829C2AB38C452E3871C209C1486E0E37BCC8FC44F447C78614BA82592DBD6D6C326BFCD60123
n = q * p


def gen_random_string(length):
    return  ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def gen_random_string_list(size, string_length):
    return [gen_random_string(string_length) for _ in range(size)]

def string_to_number(word):
    return int.from_bytes(bytearray(word, "utf8"), "big")

def pre_compute_qres(wordlist):
    t_start = time.time()

    for i in range(len(wordlist)):
        word_as_num = string_to_number(wordlist[i])
        x = (word_as_num ** 2) % n

    t_end = time.time()

    t_delta = t_end - t_start

    print(f'Precomputing QRS, time delta {t_delta}')

    return t_delta 

def pre_compute_sha1(wordlist):
    t_start = time.time()

    for i in range(len(wordlist)):
        word = wordlist[i];
        m = hashlib.sha1()
        m.update(bytearray(word, 'utf8'))
        m.digest()  

    t_end = time.time()

    t_delta = t_end - t_start

    print(f'Precomputing SHA1, time delta {t_delta}') 

    return t_delta

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # i = 101
    # print(f'P: {i}, Residues: {quadratic_residue(i)}')

    list_size = 2 ** 10
    word_lenght = 32

    print(f'Wordlist size {list_size}, string length {word_lenght}')
    print(f'Modulo n {n}')

    word_list = gen_random_string_list(list_size, word_lenght)

    pre_compute_qres(word_list)
    pre_compute_sha1(word_list)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/