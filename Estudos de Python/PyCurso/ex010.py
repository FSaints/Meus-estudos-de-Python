media = float(input('Uma distância em metros: '))
km = media / 1000
hm = media / 100
dam = media / 10
cm = media * 100
mm = media * 1000
print('A medida de {}m corresponde a {}km,{}hm, {}dam, {:.0f}cm e {:.0f}mm'.format(media, km, hm, dam, cm, mm))