#Protocolo inicial para hacer las tramas
import socket
from PVS.PVS import PVS


#crearemos al conexion principal con Ivp4 y tcp/ip


servidorPrincipal=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#creo el socket*/

#Variables Globales iniciales
direccionIp=socket.gethostbyname(socket.gethostname())
puertoDireccionamiento=50000
conexionDatos=(direccionIp,puertoDireccionamiento)#objeto con dos varibles para qye las reciba bind
conexiones=2

#luego asignamos valores al servidorPrincipal

servidorPrincipal.bind(conexionDatos)

servidorPrincipal.listen(conexiones)

p = PVS(input = 0)

rdata = []
l = 0
unfill_data = []
bytes_data = []
#creamos un ciclo para poder ver el socket trabajando
while True:
	print("Esperando conexion")
	conectar,direccionActual =servidorPrincipal.accept()
	print("nos conectamos en:%s" %(direccionActual[1]))
	print(conectar)
	#conectar.send(b'x222')
	peticion=conectar.recv(4096)
	for _ in range(1000000):
		data = conectar.recv(4096)
		rdata.append(data)

	for r in rdata:
		unfill_data.append(p.unfill_bits(r))

	for d in unfill_data:
		bytes_data.append(bytes(str(d),"utf-8"))

	for play in bytes_data:
		p.play_data(play)

	print(len(rdata))
	
	conectar.close()