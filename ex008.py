#conversor de medidas

metro = float(input('Digite uma distância em metros: '))
km = metro / 1000
cm = metro * 100
mm = metro * 1000
print('A medida de {} metro(s) equivale a:\n{}km\n{:.0f}cm\n{:.0f}mm'.format(metro, km, cm, mm))

