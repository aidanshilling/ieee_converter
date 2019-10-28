#This is a work in progress project
#Created by Aidan Shilling

from decimal import Decimal

#Global variables
count = 0
i = []
b = ''

def main ():
    #Main function
    collect_inputs()
    #normalize()

def convert_str(string):
    li = list(string)
    return li

def collect_inputs ():
    #Gets decimal number from user to covert
    dec = Decimal(input("Please enter a foating point number to convert: "))
    convert_bin(dec)
    #Coverts left side of decimal
    convert_bin_r(dec)
    #Coverts right side of decimal
    normalize()


def convert_bin (dec):
    #Converts left side of decimal into binary by continuously dividing by 2 and dumping remainder until n is less than 1
    global b

    n = int(dec)

    if n > 1:
        convert_bin(n//2)
    b += (str(n%2))
        #Adds values to string b


def convert_bin_r (dec):
    #Coverts right side of decimal by multiplying by 2 then checking to see if the answer is less than or greater than zero
    #If less than zero, a 0 is added to a list, if greater but less than 2, a 1 is added
    global count
    global i
    global b
    n_l = int(dec)
    n = dec - n_l
    
    if n*2 < 1:
        i.append(0)
        count = count + 1
    elif n*2 < 2:
        i.append(1)
        count = count + 1
    else:
        i.append('null')
    
    if count < 23:
        #This limits the number to 23 decimal places as specified in a 32 IEEE754 system
        convert_bin_r(n*2)
    else:
        #Adds values to string b
        b += ('.')
        for elem in i:
            b += (str(elem))


def normalize ():
    global b
    count_l = 0
    count_r = 0

    dec = 0

    switch = False

    b_n = []

    for char in b:
        if char != '.':
            if switch == False:
                count_l+=1
            elif switch:
                count_r+=1
        else:
            dec = char
    
    #do stuff

    b_n = convert_str(b)
    #puts characters from string b into list b_n
    b_n.remove(dec)


#Get MSB & find the e (look this up)


main()
#runs main funtion
print(b)
#prints answer



#Conversion process
#DONE
# 1. Convert to Binary
#TODO
# 2. Incorporate MSB
# 3. Normalize
# 4. Hide MSB
# 5. Excess 128 Exponent???




