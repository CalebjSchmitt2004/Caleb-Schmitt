import random
import sys
import os
import time


class methods:
    def __init__(self):
        print("\n")

    def start_sys(self):
        sys_start = input("Start System?:(Y/N) ")
        if sys_start == "Y":
            self.welcome()
        else:
            print("Good Bye")
            sys.exit()

    def welcome(self):
        Contributors = "Caleb Schmitt"
        space = "\n"

        os.system("cls")
        print("Welcome to the Computer Networking Network Help AI")
        print(space, space)
        print("This AI was developed by " + Contributors)
        print(space)
        print(
            "This AI's main purpose is to help new and incoming first year students with understanding some of the " + space +
            "more challenging subjects in this class. If you have any further questions or concerns with the class or " + space +
            "please feel free to ask the Computer Networking group chat on Slack.")

    def loading_anim(self):
        print("\n")
        print("Loading System")
        animation = [
            "[        ]",
            "[=       ]",
            "[===     ]",
            "[====    ]",
            "[=====   ]",
            "[======  ]",
            "[======= ]",
            "[========]",
            "[ =======]",
            "[  ======]",
            "[   =====]",
            "[    ====]",
            "[     ===]",
            "[      ==]",
            "[       =]",
            "[        ]",
            "[        ]"
        ]
        notcomplete = True

        i = 0

        while notcomplete:
            print(animation[i % len(animation)], end='\r')
            time.sleep(.1)
            i += 1
            if i == 17 * 20:
                break

    def run_program(self):
        self.loading_anim()
        os.system("cls")
        print("\n If you are confused please type out (!help)")
        what_to_do = input("What subject can I help you with today?: ")

        if what_to_do == "!help":
            list_help = ["subnetting", "number_conversion, n_and_s_bridge_differences", "network_cable_identifier"]
            print(list_help)

        if what_to_do == "subnetting":
            self.run_subnetting()

        if what_to_do == "number_conversion":
            self.run_number_convertion()

        if what_to_do == "n_and_s_bridge_differences":
            self.run_north_and_south_differences()

        if what_to_do == "network_cable_identifier":
            self.run_network_cable_identifer()

    def run_subnetting(self):
        info = self.get_info()
        binary = self.find_binary(info)
        adding = self.find_adding(binary)
        Decimal = self.find_decimal(adding)

        result = (str(adding[0]) + "." + str(adding[1]) + "." + str(adding[2]) + "." + str(adding[3]))

        print("\nAdding Result in Binary: " + result)
        print("\nAdding result in Decimal: " + str(Decimal))

        print("\nBits Borrowed: " + str(self.bits_barrowed(binary[1])))

    def get_info(self):
        ip_address = input("What is the Hosts Ip Address?: ")
        subnet_mask = input("what is the Subnet Mask Address?: ")

        # Separates Octets of the IP address
        separate_ip_octets = ip_address.split(".")

        first_ip_octet = int(separate_ip_octets[0])
        second_ip_octet = int(separate_ip_octets[1])
        third_ip_octet = int(separate_ip_octets[2])
        forth_ip_octet = int(separate_ip_octets[3])
        # End of Ip

        # Separates Octets of the Subnet Mask
        separate_mask_octets = subnet_mask.split(".")

        first_mask_octet = int(separate_mask_octets[0])
        second_mask_octet = int(separate_mask_octets[1])
        third_mask_octet = int(separate_mask_octets[2])
        forth_mask_octet = int(separate_mask_octets[3])
        # End of Mask

        all_ip = (first_ip_octet, second_ip_octet, third_ip_octet, forth_ip_octet)
        all_mask = (first_mask_octet, second_mask_octet, third_mask_octet, forth_mask_octet)

        return all_ip, all_mask

    def find_binary(self, i):
        ip_binary = i[0]
        mask_binary = i[1]

        first_binary_octet_ip = self.get_binary(ip_binary[0])
        second_binary_octet_ip = self.get_binary(ip_binary[1])
        third_binary_octet_ip = self.get_binary(ip_binary[2])
        forth_binary_octet_ip = self.get_binary(ip_binary[3])

        first_binary_octet_mask = self.get_binary(mask_binary[0])
        second_binary_octet_mask = self.get_binary(mask_binary[1])
        third_binary_octet_mask = self.get_binary(mask_binary[2])
        forth_binary_octet_mask = self.get_binary(mask_binary[3])

        all_binary_ip = first_binary_octet_ip, second_binary_octet_ip, third_binary_octet_ip, forth_binary_octet_ip
        all_binary_mask = first_binary_octet_mask, second_binary_octet_mask, third_binary_octet_mask, forth_binary_octet_mask

        return all_binary_ip, all_binary_mask

    def get_binary(self, i):
        num = i
        binary_return = ""

        num_list = [128, 64, 32, 16, 8, 4, 2, 1]

        Int = 0
        while Int <= 7:
            if num >= num_list[Int]:
                num -= num_list[Int]
                binary_return += "1"
            else:
                binary_return += "0"

            Int += 1
        return binary_return

    def find_adding(self, a):
        ip_adding = a[0]
        mask_adding = a[1]

        first_octet_adding_ip = self.split_binary(ip_adding[0])
        second_octet_adding_ip = self.split_binary(ip_adding[1])
        third_octet_adding_ip = self.split_binary(ip_adding[2])
        forth_octet_adding_ip = self.split_binary(ip_adding[3])

        split_binary_ip = first_octet_adding_ip, second_octet_adding_ip, third_octet_adding_ip, forth_octet_adding_ip

        first_octet_adding_mask = self.split_binary(mask_adding[0])
        second_octet_adding_mask = self.split_binary(mask_adding[1])
        third_octet_adding_mask = self.split_binary(mask_adding[2])
        forth_octet_adding_mask = self.split_binary(mask_adding[3])

        split_binary_mask = first_octet_adding_mask, second_octet_adding_mask, third_octet_adding_mask, forth_octet_adding_mask

        return self.get_adding((split_binary_ip, split_binary_mask))

    def split_binary(self, i):
        i = [char for char in i]
        return i

    def get_adding(self, diget):
        ip_binary_split = diget[0]
        mask_binary_split = diget[1]

        first_ip_octet_adding = self.Adding(ip_binary_split[0], mask_binary_split[0])
        second_ip_octet_adding = self.Adding(ip_binary_split[1], mask_binary_split[1])
        third_ip_octet_adding = self.Adding(ip_binary_split[2], mask_binary_split[2])
        forth_ip_octet_adding = self.Adding(ip_binary_split[3], mask_binary_split[3])

        network_address = [first_ip_octet_adding, second_ip_octet_adding, third_ip_octet_adding, forth_ip_octet_adding]

        return network_address

    def Adding(self, ip_a, mask_a):
        adding_result = ""
        I = 0
        while I <= 7:
            if ip_a[I] == '1' and mask_a[I] == '1':
                adding_result += "1"
            else:
                adding_result += "0"

            I += 1

        return adding_result

    def find_decimal(self, l):
        binary_to_decimal_o_1 = self.to_decimal(l[0])
        binary_to_decimal_o_2 = self.to_decimal(l[1])
        binary_to_decimal_o_3 = self.to_decimal(l[2])
        binary_to_decimal_o_4 = self.to_decimal(l[3])

        DECIMAL = str(binary_to_decimal_o_1) + "." + str(binary_to_decimal_o_2) + "." + str(
            binary_to_decimal_o_3) + "." + str(binary_to_decimal_o_4)

        return DECIMAL

    def to_decimal(self, f):
        separate_of_digits = self.split_binary(f)

        binary_nums = (128, 64, 32, 16, 8, 4, 2, 1)

        decimal_sum = 0

        q = len(separate_of_digits)
        for index in range(q):
            if separate_of_digits[index] == "1":
                decimal_sum += binary_nums[index]

        return decimal_sum

    def bits_barrowed(self, mask):
        host = self.split_binary(mask[3])

        bits = 0

        output = 0
        while output <= 5:
            if host[output] == "1":
                bits += 1
                output += 1
            else:
                output = 6

        return bits

    def to_decimal(self, num):
        From = input("Is this a binary number or a hex number?: ")
        if From == "binary":
            return int(num, 2)
        if From == "hex":
            return int(num, 16)

    def decimalToBinary(self, n):
        return bin(n).replace("0b", " ")

    def to_binary(self, num):
        From = input("Is this a decimal number or a hex number?: ")
        if From == "decimal":
            return self.decimalToBinary(int(num, 10))
        if From == "hex":
            return self.decimalToBinary(int(num, 16))

    def to_hex(self, num):
        return hex(int(num, 10))

    def run_number_convertion(self):
        number = input("Please input the number you would like to convert: ")
        to_what = input("What would you like this number converted into:(In lower case) ")
        print("\n If you are confused type (list_options) for the conversion type")

        if to_what == "list_options":
            options = ["decimal", "binary", "hex"]
            print(options)

        if to_what == "decimal":
            print(self.to_decimal(number))
        if to_what == "binary":
            print(self.to_binary(number))
        if to_what == "hex":
            print(self.to_hex(number))

    def run_north_and_south_differences(self):
        os.system("cls")
        print("If you would like a list of options just type (list_options)")
        print("Please input all answers in lower case")
        start = input("\n What bridge do you need more help with?: ")

        if start == "list_options":
            print("north, south, both")

        if start == "north":
            for i in range(16):
                self.north()

        if start == "south":
            for i in range(16):
                self.south()

        if start == "both":
            for i in range(8):
                self.north()
                self.south()

    def north(self):
        key = [["What chip is located at the north end of the board?", "north"], ["What chip is bigger?", "north"],
               ["What chip communicates faster?", "north"], ["What chip is connected directly to the CPU?", "north"],
               ["What chip communicates using FSB?", "north"], ["Which chip controls adapter cards?", "north"],
               ["Which chip is the hub for memory control?", "north"]]
        questions = random.sample(key, len(key))

        q = 0
        a = 0

        while q <= len(questions):
            while a <= len(questions):
                question = questions[q][0]
                print("\n" + question)
                answer = input("")

                if answer == questions[a][1]:
                    print("Good job")
                else:
                    print("Oops Sorry")
                    print("\n Corrects Answer: ")
                    print(questions[a][1])

                q += 1
                a += 1

    def south(self):
        key = [["What chip is located at the south end of the board?", "south"],
               ["What chip is the hub for USB?", "south"], ["Which chip manages power?", "south"],
               ["Which chip has plug and play support?", "south"],
               ["What chip controls IDE and ATA Interfaces?", "south"], ["What chip is smaller?", "south"],
               ["Which chip handles I/O support?", "south"]]
        questions = random.sample(key, len(key))

        q = 0
        a = 0

        while q <= len(questions):
            while a <= len(questions):
                question = questions[q][0]
                print("\n" + question)
                answer = input("")

                if answer == questions[a][1]:
                    print("Good job")
                else:
                    print("Oops Sorry")
                    print("\n Corrects Answer: ")
                    print(questions[a][1])

                q += 1
                a += 1

    def run_network_cable_identifer(self):
        print("Please input all of you answers in lower case and separate all multi answer questions with a comma no space")
        print("If you are confused or need help type list_options")
        answer = input("What cable would you like to practice on?: ")

        if answer == "list_options":
            options = ["strait, cross-over, roll-over"]
            print(options)

        if answer == "strait":
            self.strait()

        if answer == "cross-over":
            self.cross_over()

        if answer == "roll_over":
            self.roll_over()

    def strait(self):
        side_one = ["white-orange", "orange", "white-green", "blue", "white-blue", "green", "white-brown", "brown"]
        side_two = ["white-orange", "orange", "white-green", "blue", "white-blue", "green", "white-brown", "brown"]

        points = 0

        index = 1
        side = 1

        side_one_color_list = []
        side_two_color_list = []

        while index <= 16:
            answer = input("What is the color of side " + str(side) + " pin " + str(index))
            side_one_color_list.append(answer)
            if index <= 8:
                side_one_color_list.append(answer)
            if index == 8:
                print("\n")
                side += 1
            if index > 16 & index <= 16:
                side_two_color_list.append(answer)

        i = 0

        while i <= 7:
            if side_one_color_list[i] == side_one[i]:
                points += 1
            else:
                print(side_one[i])
            if side_two_color_list[i] == side_two[i]:
                points += 1
            else:
                print(side_two[i])

        print("You got " + str(16 - points) + " wrong")
        print("Your finally score is " + str(points) + "/20")

    def cross_over(self):
        side_one = ["white-orange", "orange", "white-green", "blue", "white-blue", "green", "white-brown", "brown"]
        side_two = ["white-green", "green", "white-orange", "blue", "white-blue", "orange", "white-brown", "brown"]

        points = 0

        index = 1
        side = 1

        side_one_color_list = []
        side_two_color_list = []

        while index <= 16:
            answer = input("What is the color of side " + str(side) + " pin " + str(index))
            side_one_color_list.append(answer)
            if index <= 8:
                side_one_color_list.append(answer)
            if index == 8:
                print("\n")
                side += 1
            if index > 16 & index <= 16:
                side_two_color_list.append(answer)

        i = 0

        while i <= 7:
            if side_one_color_list[i] == side_one[i]:
                points += 1
            else:
                print(side_one[i])
            if side_two_color_list[i] == side_two[i]:
                points += 1
            else:
                print(side_two[i])

        print("You got " + str(16 - points) + " wrong")
        print("Your finally score is " + str(points) + "/20")

    def roll_over(self):
        side_one = ["white-orange", "orange", "white-green", "blue", "white-blue", "green", "white-brown", "brown"]
        side_two = ["brown", "white-brown", "green", "white-blue", "blue", "white-green", "orange", "white-orange"]

        points = 0

        index = 1
        side = 1

        side_one_color_list = []
        side_two_color_list = []

        while index <= 16:
            answer = input("What is the color of side " + str(side) + " pin " + str(index))
            side_one_color_list.append(answer)
            if index <= 8:
                side_one_color_list.append(answer)
            if index == 8:
                print("\n")
                side += 1
            if index > 16 & index <= 16:
                side_two_color_list.append(answer)

        i = 0

        while i <= 7:
            if side_one_color_list[i] == side_one[i]:
                points += 1
            else:
                print(side_one[i])
            if side_two_color_list[i] == side_two[i]:
                points += 1
            else:
                print(side_two[i])

        print("You got " + str(16 - points) + " wrong")
        print("Your finally score is " + str(points) + "/20")
