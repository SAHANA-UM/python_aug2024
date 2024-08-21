#Program to Print Math table of a number

input_num = int (input('Enter a number to print its Math table: '))

for i in range(1,16):
    #print(input_num,'*',i,'=',input_number*i)
    print('%02d * %02d = %03d' %(input_num,i,input_num*i))
   