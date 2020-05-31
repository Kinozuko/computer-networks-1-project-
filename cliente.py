import socket
import time
from PVS.PVS import PVS
#
servidorPrincipal=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


direccionIp=socket.gethostbyname(socket.gethostname())
puertoDireccionamiento=50000
conexionDatos=(direccionIp,puertoDireccionamiento)
servidorPrincipal.connect(conexionDatos)

print("conectando a %s "%(direccionIp))

record = PVS()
record.start_stream()

frames_bit = record.convert_to_bin(record.record())
fill_bits_frames = []
fill_bits_bytes_frames = []

for fbits in frames_bit:
	fill_bits_frames.append(record.fill_bits(fbits))

for fbits in fill_bits_frames:
    fill_bits_bytes_frames.append(bytes(fbits,"utf-8"))

for fbits in fill_bits_bytes_frames:
	servidorPrincipal.send(fbits)
	time.sleep(2)

#esta es la respuesta del servidor con recv y 1024 bits de buffer
respuesta=servidorPrincipal.recv(1024)

print(respuesta)

servidorPrincipal.close()