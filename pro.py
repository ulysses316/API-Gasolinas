import requests

class Combustible:
    def distancia(self,o,d,rendimiento):
        a=requests.get(params={"origins": o, "destinations":d}, url="https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&key=[INSERTA TU KEY]").json()
        print "La distancia entre los destinos es: ",a["rows"][0]["elements"][0]["distance"]["text"]
        print "El tiempo estimado de viaje es: ",a["rows"][0]["elements"][0]["duration"]["text"]
        km=a["rows"][0]["elements"][0]["distance"]["text"]
        km=km.split(" ")
        self.km=float(km[0])
        self.combustible= self.km/rendimiento
        print "El combustible necesario para llegar a "+ str(d)+" es de "+str(self.combustible)
        origen=a["destination_addresses"]
        destino=a["origin_addresses"]
        print origen[0]
        print destino[0]


o=raw_input("Dame el punto de origen: ")
d=raw_input("Dame el destino deseado: ")
rendimiento=float(raw_input("Dame el rendimiento de combustible de tu automovil en km/l: "))
com=Combustible()
com.distancia(o,d,rendimiento)
