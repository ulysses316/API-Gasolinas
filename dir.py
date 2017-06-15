import requests
class Agotamiento():
    def punto_de_alerta_de_combustible_bajo(self,rendimieto,captanque,tanque):
        self.combustible= captanque*tanque
        self.agotamiento=self.combustible*rendimieto
        suma=0
        o=raw_input("Dame el punto de origen: ")
        d=raw_input("Dame el destino deseado: ")
        a=requests.get(params={"origin": o, "destination":d}, url="https://maps.googleapis.com/maps/api/directions/json?key=[INSERTA TU KEY]").json()
        lista=a["routes"][0]["legs"][0]["steps"]
        for x in lista:
            latitud=x["start_location"]["lat"]
            longitud=x["start_location"]["lng"]
            dis=x["distance"]["text"]
            dis=dis.split(" ")
            if dis[1]== "m":
                dis=float(dis[0])/1000
                if self.agotamiento<suma:
                    break
                suma+=dis
                else:
                dis=float(dis[0])
                if self.agotamiento<suma:
                    break
                suma+=dis
        if suma<self.agotamiento:
            print "ALcanzas a llegar a tu destino sin poblemas"
        else:
            self.latlng=str(latitud)+","+str(longitud)
            print "Las coordenadas son: "+str(self.latlng)+" se esta buscando las gasolineras mas cercanas al punto de alerta de combustible"
            ago.places(self.latlng)
    def places(self,latlng):
        a=requests.get(params={"query":"gasolineras","location":latlng,"radius":"10000","key":"AIzaSyDpXg00OMh_CzAN3I8zxMIeziwcZx9XrX8"}, url="https://maps.googleapis.com/maps/api/place/textsearch/json").json()
        print"\n\n\n"
        print("La primera gasolinera mas cercana es:")
        print a["results"][0]["formatted_address"]
        print("La segunda gasolinera mas cercana es:")
        print a["results"][1]["formatted_address"]
        print("La tercera gasolinera mas cercana es:")
        print a["results"][2]["formatted_address"]
        print("La cuarta gasolinera mas cercana es:")
        print a["results"][3]["formatted_address"]
        print("La quinta gasolinera mas cercana es:")
        print a["results"][4]["formatted_address"]
print "\t\t\t\t\t\t\t\tServicio 2"
rendimiento=float(raw_input("\n\nDame el rendimiento de gasolina de tu automovil en km/l: "))
captanque=float(raw_input("Dame la capacidad de tu tanque de gasolina "))
tanque=float(raw_input("Dame en fraccion la cantidad de gasolina con la cual dispones "))
ago=Agotamiento()
ago.punto_de_alerta_de_combustible_bajo(rendimiento,captanque,tanque)
