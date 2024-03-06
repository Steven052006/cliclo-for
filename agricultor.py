papa=0
yuca=0
zanahoria=0
tipo_de_tuberculo = int (input ("1/papa 2/yuca 3/zanahoria"))
if tipo_de_tuberculo == 1:
    for i in range (3) :
        litros=int(input ("cuantos litros gastaste hoy:"))
        papa += litros
    print ("los litros gastados esta semana fueron:", papa)   

if tipo_de_tuberculo == 2:
    for i in range (2) :
        litros=int(input ("cuantos litros gastaste hoy:"))
        yuca += litros
    print ("los litros gastados esta semana fueron:", yuca)   

if tipo_de_tuberculo == 3:
    for i in range (2) :
        litros=int(input ("cuantos litros gastaste hoy:"))
        zanahoria += litros
    print ("los litros gastados esta semana fueron:", zanahoria)      