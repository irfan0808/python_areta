#cara mendefinisikan list
sebuah_list=['ZorinOS',
            'Ubuntu',
            'FreeBSD',
            'NetBSD',
            'OpenBSD',
            'Backtrack',
            'Fedora',
            'Slackwere',]

#cara mendefinisikan tuple
sebuah_tuple=('0','1','2','3','4','5','6','7','8','9')

#cara mendefinisikan sebuah Dictionary
sebuah_dictionary={'Nama':'Wiro Sableng',
                   'Prodi':'Ilmu Komputer',
                   'Email':'wirosabkeng@localhost',
                   'website':'http://www.sipampanggarang.com'}

print sebuah_list
print sebuah_tuple
print sebuah_dictionary

#cara akses list
print sebuah_list[2:7]

#cara akses tuple
print sebuah_tuple[3:6]

#cara akses dictionary
print sebuah_dictionary['Nama']
print sebuah_dictionary['website']



for sebuah in sebuah_list:
    print sebuah,
print "\n"


for sebuah in sebuah_tuple:
    print sebuah,
print "\n"

for sebuah in sebuah_dictionary:
    print sebuah,':',sebuah_dictionary[sebuah]