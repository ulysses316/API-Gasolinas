class Principal:
    def servicio(self, serv):
        if serv=="1":
            import pro
print "\n\n\t\t\t\t\t\t Servicios referentes al consumo de combustible"
print"\n\n\t\t\t 1.- Numero total de gasolina necesaria para ir de un lugar a otro y costo"
print"\t\t\t 2.- Tiempo teorico de consumo total de combustible"
print"\t\t\t 3.-  "

serv=raw_input("Que numero de servicio quieres utilizar? ")
pri=Principal()
pri.servicio(serv)
