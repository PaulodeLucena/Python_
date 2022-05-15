print('Conversor de metros')

medida = float(input('Digite a metragem: '))

km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('A medida digitada foi {:.0f}m, corresponde a {:.0f}km, {:.0f}hm, {:.0f}dam, {:.0f}dm, {:.0f}cm, {:.0f}mm. '.format(medida, km, hm, dam, dm, cm, mm))

