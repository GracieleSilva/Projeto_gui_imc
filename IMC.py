# -*- coding: utf-8 -*-

import PySimpleGUI as sg

def isnumber(value):
	try:
		float(value)
	except ValueError:
		return False
	return True

def calcula_imc(altura=0, peso=0, sexo=''):
	"""IMC = 90.5 kg / (170 cm)2 -> IMC = 31.3"""
	IMC = float(peso)/(float(altura)*float(altura))
	MSG = ""
	if sexo == 'M' or sexo == 'm':
		if IMC <= 19.0:
			MSG = "Abaixo do peso"
		elif  IMC >=19.1 and IMC <=24.0:
			MSG = "Normal"
		elif IMC >=24.1 and IMC <=29:
			MSG = "Sobrepeso"
		elif IMC >=29.1 and IMC <=38.9:
			MSG = "Obeso"
		else:
			MSG = "Obeso mórbido"
		#MSG += ", M O seu peso ideal e {:.2f}".format((72.2*altura) - 57)
	elif sexo == 'F' or sexo == 'f':
		if IMC <= 18.0:
			MSG = "Abaixo do peso"
		elif  IMC >=18.1 and IMC <=23.0:
			MSG = "Normal"
		elif IMC >=23.1 and IMC <=28:
			MSG = "Sobrepeso"
		elif IMC >=28.1 and IMC <=37.9:
			MSG = "Obeso"
		else:
			MSG = "Obeso mórbido"
		#MSG += ", O seu peso ideal e {:.2f}".format((62.1*altura)-44.7)
	else:
		MSG = "Sexo Nao Informado! "
	return IMC,MSG


def imc_gui(layout, titulo):
	window = sg.Window(titulo).Layout(layout)
	while True:
		event, values = window.Read()
		if event is None or event == 'Exit':
			break
		if event == '-BTN-IMC-':
			altura  = values['-altura-'].replace(',','.')
			peso    = values['-peso-'].replace(',','.')

			if isnumber(altura) and isnumber(peso):

				imc = calcula_imc(altura, peso, values['-sexo-'])  # Mudar para funcao do colega 
				
				print(imc)
				window['-OUTPUT-'].update('Seu IMC e {:.2f}, voce esta {}'.format(imc[0],imc[1])) # mudar aqui tambem
			else:
				window['-OUTPUT-'].update('Campos Vazios ou ñ numerico!')

	window.Close()

if __name__ == '__main__':
	sg.theme('Dark Brown')
	layout = [  
		[sg.Text('Peso'+':', justification='r', size=(5,1)), sg.In(key='-peso-', size=(5,1)),sg.Text('Peso em Kg')],
		[sg.Text('Altura'+':', justification='r', size=(5,1)), sg.In(key='-altura-', size=(5,1)),sg.Text('Altura em metros')],
		[sg.Text('Sexo'+':', justification='r', size=(5,1)),sg.Combo(list(['M','F']),default_value='M', enable_events=True, size=(20,1), key='-sexo-')],
		[sg.Text(size=(40,1), key='-OUTPUT-')],
		[sg.Button('Caucula IMC',key='-BTN-IMC-'), sg.Button('Exit')]
	]

	imc_gui(layout, 'Calculo de IMC')