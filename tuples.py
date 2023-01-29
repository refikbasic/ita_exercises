tapl1=("jedan","dva","tri")
tapl2=("mujo","haso","suljo")
tapl3=("crvena","crna","plava")
tapl1novi=list(tapl1)
tapl1novi.append("ITAkademija")
tapl1=tuple(tapl1novi)
print(tapl1)
del tapl2
del tapl3
tapl4=("novi","najnoviji","josnoviji")
tapl5=tapl1+tapl4
print(tapl5)