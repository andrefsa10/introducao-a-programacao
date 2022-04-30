VET=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,5,25,26,27,28,29,30,31,32,5,34,35,36,37,38,39,40,41,42,43,44,45,5,47,48,49,50]
for num in VET:
  if VET.count(num)>1:
    print(f'O número {num} se repete {VET.count(num)} vezes nas posições {VET.index(5)}, {VET.index(5,2)}, {VET.index(5,24)}, {VET.index(5,34)}')
    break

