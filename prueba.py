import requests

def places():
    o=raw_input("Dame el lugar en el que deseas operar: ")
    a=requests.get(params={"query":"gasolineras","location":o,"radius":"10000","key":"[INSERTA TU KEY]"}, url="https://maps.googleapis.com/maps/api/place/textsearch/json").json()
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
places()
