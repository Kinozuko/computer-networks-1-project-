'''
	PVS Class

	Python Voice Signal

	Clase para captar y reproducir audio

	@author Victor Mendoza 
'''

try:
	import pyaudio
except:
	print("Error de importacion")


class PVS(object):
	# Constructor del objecto PVS
	def __init__(self, input = 1, format = pyaudio.paInt32, channels = 2, rate = 44100, chunk = 4096):
		self.device = pyaudio.PyAudio()
		self.input = input
		if input:
			self.stream = self.device.open(format = format,
											channels = channels,
											rate = rate, 
											input = True
										)
		else:
			self.stream = self.device.open(format = format,
											channels = channels,
											rate = rate,
											output = True
										)
		self.CHUNK = chunk

	def start_stream(self):
		if self.input:
			self.stream.start_stream()
		else:
			print("El objeto solo puede captar senales\n")

	def get_input_data(self):
		if self.input:
			return self.stream.read(self.CHUNK)
		else:
			print("El objeto solo puede captar senales\n")

	def play_data(self,data):
		if self.input:
			print("El objeto solo puede reproducir senales\n")
		else:
			self.stream.write(data)

	def record(self):
		print("\n\n\n ctrl + c para salir")

		frame = []

		while True:
			try:
				data = self.get_input_data()
				frame.append(data)
			except KeyboardInterrupt:
				print("Mensaje guardado")
				break
			except:
				pass

		return frame

	def convert_to_bin(self,frames):
		frames_bit = []
		for f in frames:
			for frame in f:
				frames_bit.append(bin(frame)[2:])

		return frames_bit

	def fill_bits(self,bits):
		aux_cad = ""
		i = cont_uno = 0
		while i < len(bits):
			aux_cad += bits[i]
			if bits[i] == '1':
				cont_uno += 1
			else:
				cont_uno = 0
			if cont_uno == 5:
				aux_cad = aux_cad + "0"
				cont_uno = 0
			i += 1
		return aux_cad

	def unfill_bits(self,bits):
		aux_cad = ""
		i = cont_uno = 0
		while i < len(bits):
			aux_cad += bits[i]
			if bits[i] == '1':
				cont_uno += 1
			else:
				cont_uno = 0
			if cont_uno == 5:
				i = i + 1
				cont_uno = 0
			i += 1
		return aux_cad

	def CRC(self,bits):
		G = "11001010100101011"
		residuo = bits
		auxi_res = aux = ""
		i = j = k = 0
		tam_G = len(G) - 1
		band = True
		while j < len(G) - 1:
			residuo = residuo + "0"
			j = j + 1
		aux = residuo
		i = len(residuo)
		while j < i and band:
			if j < i and band:
				j = 0
				while j<i and residuo[j] != '1':
					j = j + 1
					auxi_res = auxi_res = "0"
			if j + tam_G + 1 > i:
				band = False
			if band == True:
				k = 0
				for k in range(tam_G):
					if residuo[j] != G[k]:
						auxi_res = auxi_res + "1"
					else:
						auxi_res = auxi_res + "0"
					j = j + 1
				auxi_res = auxi_res + residuo[j:len(residuo)]
				residuo = auxi_res
				auxi_res = ""
		auxi_res = ""
		k = 0
		for k in range(len(residuo)-1):
			if residuo[k] != aux[k]:
				auxi_res = auxi_res + "1"
			else:
				auxi_res = auxi_res + "0"
		return auxi_res

	def __del__(self):
		self.stream.stop_stream()
		self.stream.close()
		self.device.terminate()
