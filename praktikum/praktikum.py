# praktikum


list_nama=[]
list_nim=[]
list_tugas=[]
list_uts=[]
list_uas=[]
list_data=[]
list_total=[]

ulang=2

for i in range(ulang):
    print ("data ke - " + str(i+1))
    list_nama.append(input("Masukan nama anda : "))
    list_nim.append(input("Masukan nim anda : "))
    list_tugas.append(int(input("Masukan nilai tugas anda :")))
    list_uts.append(int(input("Masukan nilai uts anda :")))
    list_uas.append(int(input("Masukan nilai uas anda :")))

for i in range(ulang):
    list_total.append((list_tugas[i] + list_uts[i] + list_uas[i] /3 ))

print("====================================================")
print("Nama     Nim     Tugas     UTS     UAS     Total")
print("====================================================")

for i in range(ulang):
    print ("%s \t\t %s \t %i \t\t %i \t\t\t %i" % (list_nama[i], list_tugas[i], list_uts[i], list_uas[i], list_total[i]))
print("====================================================")
