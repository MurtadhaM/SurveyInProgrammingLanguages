import os
import readline


def input_parser(filename):
    file = open(filename)
    number_valid = 0
    for input in file.readlines():

        try:
            letters_found = 0
            at_least = int(input.split('-')[0].split(' ')[0])
            at_most = int(input.split('-')[1].split(' ')[0])
            letter = input.split(':')[0].split(' ')[1]
            password = input.split(':')[1]

            # print(at_least)
            # print(at_most)
            # print(letter)
            # print(password)

            for l in password:
                if l == letter:
                    letters_found = letters_found + 1

            if letters_found in range(at_least, at_most + 1):
                # print(input)
                number_valid = number_valid + 1
                print(number_valid)
                print(input)


        except Exception as e:
            print(e)
    # print(number_valid)


def input_parser_2(filename):
    file = open(filename)
    number_valid = 0
    for input in file.readlines():

        try:
            letters_found = 0
            position_first = int(input.split('-')[0].split(' ')[0])
            position_second = int(input.split('-')[1].split(' ')[0])
            letter = input.split(':')[0].split(' ')[1]
            password = input.split(':')[1]

            # print(at_least)
            # print(at_most)
            # print(letter)
            # print(password)

            if ((password[position_first] == letter and (password[position_second] != letter)) or (
            (password[position_first] != letter and (password[position_second] == letter)))):
                number_valid = number_valid + 1




        except Exception as e:
            print(e)
    print(number_valid)


input_parser_2('input.txt')
