szam=int(input('Kérek egy számot ami pozitív és páros vagy negatív és páratlan. '))

if szam %2 ==0 and szam >= 0:
    print(f'A beadot száma pozitív és páros, {szam}.')
    
if szam %2 !=0 and szam <= 0:
    print(f'A beadot száma negatív és páratlan, {szam}.')


