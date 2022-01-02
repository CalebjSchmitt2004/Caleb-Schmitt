# start of code
def run():
    info = get_info()
    binary = find_binary(info)
    adding = find_adding(binary)
    decimal = find_decimal(adding)

    result = (str(adding[0]) + "." + str(adding[1]) + "." + str(adding[2]) + "." + str(adding[3]))

    print("\nAdding Result in Binary: " + result)
    print("\nAdding result in Decimal: " + str(decimal))
    
    print("\nBits Barrowed: " + str(bits_barrowed(binary[1])))

def get_info():
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


def find_binary(i):
    ip_binary = i[0]
    mask_binary = i[1]

    first_binary_octet_ip = get_binary(ip_binary[0])
    second_binary_octet_ip = get_binary(ip_binary[1])
    third_binary_octet_ip = get_binary(ip_binary[2])
    forth_binary_octet_ip = get_binary(ip_binary[3])

    first_binary_octet_mask = get_binary(mask_binary[0])
    second_binary_octet_mask = get_binary(mask_binary[1])
    third_binary_octet_mask = get_binary(mask_binary[2])
    forth_binary_octet_mask = get_binary(mask_binary[3])

    all_binary_ip = first_binary_octet_ip, second_binary_octet_ip, third_binary_octet_ip, forth_binary_octet_ip
    all_binary_mask = first_binary_octet_mask, second_binary_octet_mask, third_binary_octet_mask, forth_binary_octet_mask

    return all_binary_ip, all_binary_mask


def get_binary(i):
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


def find_adding(a):
    ip_adding = a[0]
    mask_adding = a[1]

    first_octet_adding_ip = split_binary(ip_adding[0])
    second_octet_adding_ip = split_binary(ip_adding[1])
    third_octet_adding_ip = split_binary(ip_adding[2])
    forth_octet_adding_ip = split_binary(ip_adding[3])

    split_binary_ip = first_octet_adding_ip, second_octet_adding_ip, third_octet_adding_ip, forth_octet_adding_ip

    first_octet_adding_mask = split_binary(mask_adding[0])
    second_octet_adding_mask = split_binary(mask_adding[1])
    third_octet_adding_mask = split_binary(mask_adding[2])
    forth_octet_adding_mask = split_binary(mask_adding[3])

    split_binary_mask = first_octet_adding_mask, second_octet_adding_mask, third_octet_adding_mask, forth_octet_adding_mask

    return get_adding((split_binary_ip, split_binary_mask))


def split_binary(i):
    i = [char for char in i]
    return i


def get_adding(diget):
    ip_binary_split = diget[0]
    mask_binary_split = diget[1]

    first_ip_octet_adding = Adding(ip_binary_split[0], mask_binary_split[0])
    second_ip_octet_adding = Adding(ip_binary_split[1], mask_binary_split[1])
    third_ip_octet_adding = Adding(ip_binary_split[2], mask_binary_split[2])
    forth_ip_octet_adding = Adding(ip_binary_split[3], mask_binary_split[3])

    network_address = [first_ip_octet_adding, second_ip_octet_adding, third_ip_octet_adding, forth_ip_octet_adding]

    return network_address


def Adding(ip_a, mask_a):
    adding_result = ""
    I = 0
    while I <= 7:
        if ip_a[I] == '1' and mask_a[I] == '1':
            adding_result += "1"
        else:
            adding_result += "0"

        I += 1

    return adding_result


def find_decimal(l):
    binary_to_decimal_o_1 = to_decimal(l[0])
    binary_to_decimal_o_2 = to_decimal(l[1])
    binary_to_decimal_o_3 = to_decimal(l[2])
    binary_to_decimal_o_4 = to_decimal(l[3])

    decimal = str(binary_to_decimal_o_1) + "." + str(binary_to_decimal_o_2) + "." + str(binary_to_decimal_o_3) + "." + str(binary_to_decimal_o_4)

    return decimal


def to_decimal(f):
    separate_of_digits = split_binary(f)

    binary_nums = (128, 64, 32, 16, 8, 4, 2, 1)

    decimal_sum = 0

    q = len(separate_of_digits)
    for index in range(q):
        if separate_of_digits[index] == "1":
            decimal_sum += binary_nums[index]

    return decimal_sum

def bits_barrowed(mask):
    host = split_binary(mask[3])
    
    bits = 0
    
    output = 0
    while output <= 5:
        if host[output] == "1":
            bits += 1
            output += 1
        else: 
            output = 6
    
    return bits
    
run()