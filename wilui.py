diasDaSemana={
'segunda':0,
    'terça':1,
    'quarta':2,
    'quinta':3,
    'sexta':4,
    'sabado':5,
    'domingo':6
}
quediaehoje=str(input("que dia e hoje"))


dia=diasDaSemana[quediaehoje]

diff = 5 - dia
if diff == 0 or diff == -1:
    print("ja e final de semana")
else:
    print(f'falta {diff}pro final de semana ')