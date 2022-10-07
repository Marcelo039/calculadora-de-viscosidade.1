from funcao import viscosidade
from PySimpleGUI import PySimpleGUI as sg

#layout
sg.theme('Reddit')
layout=[ 

[sg.Text('Digite a massa da esfera[Kg]:'),sg.Input(key='Digite a massa da esfera[Kg]:')],
[sg.Text('Digite o raio da esfera[m]:'),sg.Input(key='Digite o raio da esfera[m]:')],
[sg.Text('Digite a densidade do líquido[g/ml]:'),sg.Input(key='Digite a densidade do líquido[g/ml]:')],
[sg.Text('Digite a velocidade terminal[m/s]:'),sg.Input(key='Digite a velocidade terminal[m/s]:')],
[sg.Button('Calcular viscosidade')]
]
#janela
janela=sg.Window('cálculo da viscosidade',layout)
#ler os eventos
while True:
  eventos,  valores = janela.read()
  if eventos == sg.WINDOW_CLOSED:
    break
  if eventos == "Calcular viscosidade":
    valores['Digite a massa da esfera[Kg]:'] = float(valores['Digite a massa da esfera[Kg]:'])
    valores['Digite o raio da esfera[m]:'] = float(valores['Digite o raio da esfera[m]:'])
    valores['Digite a densidade do líquido[g/ml]:'] = float(valores['Digite a densidade do líquido[g/ml]:'])
    valores['Digite a velocidade terminal[m/s]:'] = float(valores['Digite a velocidade terminal[m/s]:'])
    print(viscosidade(valores['Digite o raio da esfera[m]:'],valores['Digite a massa da esfera[Kg]:'],valores['Digite a densidade do líquido[g/ml]:'],valores['Digite a velocidade terminal[m/s]:']))

