# #1

# x = [40,100,4,5,25,10]

# def sort_list(x) :
#     x.sort()3
#     return x

# sort_list(x)


# #2

# x = [40,100,4,5,25,10]

# def max_min(x) :
#     mini = min(x)
#     maxi = max(x)
#     return print (f'nilai terkecil :{mini},sementara nilai terbesar :',maxi)

# max_min(x)


#kuis punya rai

# print("Input the first number :") 
# a = input() #angka pertama
# print("Input the operation.... (sum/substract/divide/times/power)")
# metode = input() #metode operasi
# print("Input the second number :")
# b = input() #angka kedua


# def my_calculator(metode, a, b): #fungsi kalkulator sederhana dengan 2 parameter metode, a dan b
#   if (a.isnumeric()==True) and (b.isnumeric()==True) and (metode.isascii()==True):
#     a = int(a)
#     b = int(b)
#     if metode == '+':
#         hasil = a + b
#         print('hasil penjumlahan dari',a,metode,b,'adalah', hasil)
        
#     elif metode == '-':
#         hasil = a - b
#         print('hasil pengurangan dari',a,metode,b,'adalah', hasil)

#     elif metode == 'x':
#         hasil = a * b
#         print('hasil perkalian dari',a,metode,b,'adalah', hasil)
    
#     elif metode == ':' or metode == '/':
#         hasil = a / b
#         print('hasil pembagian dari',a,metode,b,'adalah', hasil)

#     elif metode == '^' :
#         hasil = a ** b
#         print('hasil per-pangkatan dari',a,metode,b,'adalah', hasil)

#     else:
#         print('operator not found / invalid input...')
#   else:
#     print('invalid input bro..')

# my_calculator (metode,a,b)


#cek punya johan klemantan


# def calc (a,b,c):
#     if (isinstance(a,int)==True) and (isinstance(b,str)==True) and (isinstance(c,int)==True):
#         if b == '+':
#             print('Hasil pertambahan dari',a,'dan ',c,'adalah :', a+c)
#         elif b == '-':
#             print('Hasil pengurangan dari',a,'dan ',c,'adalah :', a-c)
#         elif b == 'x':
#             print('Hasil perkalian dari',a,'dan ',c,'adalah :', a*c)
#         elif b == '/':
#             print('Hasil pembagian dari',a,'dan ',c,'adalah :', a/c)
#         elif b == '^':
#             print('Hasil pemangkatan dari',a,'dan ',c,'adalah :', a**c)
#         else:
#             print(f'Operator{b} bukan termasuk operasi matematika')
#     else :
#         print('Invalid input')

# calc (1,'x',2)


#cek punya brian rizadhani

# def calculate (x,o,y):
#     if (x.isnumeric() == True) and (o.isascii() == True) and (y.isnumeric() == True):
#         x = float(x)
#         y = float(y)
#         if o == '^': 
#             hasil = x**y
#             operasi = 'pangkat'            
#         elif o == '+':
#             hasil = x+y
#             operasi = 'penjumlahan'            
#         elif o == '-':
#             hasil = x-y
#             operasi = 'pengurangan'            
#         elif o == 'x':
#             hasil = x*y 
#             operasi = 'pengalian'            
#         elif o == '/':
#             hasil = x/y
#             operasi = 'pembagian'           
#         else:
#             hasil = 'Operators not found!'
#             operasi = ''
#     else:
#         print('Wrong input')
#         hasil = 'Tidak ada'
#         operasi = 'Tidak beroperasi'
#     return hasil, operasi
    
# x = input('Angka 1: ')
# y = input('Angka 2: ')
# o = input('Operasi perhitungan (+,-,x,/,^): ')
# hasil, operasi = calculate(x,o,y)
# print(f'Hasil {operasi} = {hasil}')



#cek punya bagus zulfikar

# par1 = int(input('angka pertama:'))
# par2 = input('operator (+,-,*,/,^):')
# par3 = int(input('angka kedua:'))
# y = int(input('angka pangkat:'))

def kalkulator(par1, par2, par3):
    if par2 == '+':
        print('hasil penambahan dari', par1, par2, par3, 'adalah', par1 + par3)
        return par1 + par3
    elif par2 == '-':
        print('hasil pengurangan dari', par1, par2, par3, 'adalah', par1 - par3)
        return par1 + par3
    elif par2 == 'x':
        print('hasil perkalian dari', par1, par2, par3, 'adalah', par1 * par3)
        return par1 * par3
    elif par2 == '/':
        print('hasil pembagian dari', par1, par2, par3, 'adalah', par1 / par3)
        return par1 / par3
    elif par2 == '^':
        print('hasil pemangkatan dari', par1, par2, par3, 'adalah', par1 ** par3)
        return par1**par3
    else:
        print('invalid input')

def perhitungan_kuadrat(hasil, y):
    print('pangkat dari', f'{hasil:,}', 'adalah', f'{hasil ** y:,}')
    return (hasil ** y)

#print(f'{(perhitungan_kuadrat(kalkulator(par1,par2,par3))):,}')
print(kalkulator(perhitungan_kuadrat(2, 2), '+', perhitungan_kuadrat(3, 2)))

# perhitungan = kalkulator(2, '^', 4)
# perhitungan = kalkulator(int(input('angka pertama:')), input('operator (+,-,*,/,^):'), int(input('angka kedua:')))
# print('kuadrat dari', f'{(int(perhitungan)):,}', 'adalah', f'{(int(perhitungan ** 2)):,}')


# cek punya bagus x ben


def kalkulator(par1, par2, par3):
    if par2 == '+':
        print('hasil penambahan dari', par1, par2, par3, 'adalah', par1 + par3)
        return par1 + par3
    elif par2 == '-':
        print('hasil pengurangan dari', par1, par2, par3, 'adalah', par1 - par3)
        return par1 + par3
    elif par2 == 'x':
        print('hasil perkalian dari', par1, par2, par3, 'adalah', par1 * par3)
        return par1 * par3
    elif par2 == '/':
        print('hasil pembagian dari', par1, par2, par3, 'adalah', par1 / par3)
        return par1 / par3
    elif par2 == '^':
        print('hasil pemangkatan dari', par1, par2, par3, 'adalah', par1 ** par3)
        return par1**par3
    else:
        print('invalid input')

    def perhitungan_kuadrat(hasil, y):
        print('pangkat dari', f'{hasil:,}', 'adalah', f'{hasil ** y:,}')
        return (hasil ** y)

    return perhitungan_kuadrat

pk = kalkulator('a', '=', 'c')
print(pk)
print(pk(4, 2))