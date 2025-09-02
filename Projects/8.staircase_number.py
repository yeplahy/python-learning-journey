#start

input_str = input("Enter number 1/2 section: ")

if len(input_str) == 1:
    print("Yes")

elif len(input_str) == 2:
    ragham_aval = int(input_str[0])
    ragham_dovom = int(input_str[1])
    
    ekhtelaf = ragham_aval - ragham_dovom
    
    if abs(ekhtelaf) == 1:
        print("Yes")
    else:
        print("No")

else:
    print("No")

#finish