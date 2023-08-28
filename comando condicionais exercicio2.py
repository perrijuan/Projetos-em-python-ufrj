dia=int(input("dia\n"))
mes=int(input("mes\n"))
ano=int(input("ano\n"))

dia2=int(input("dia\n"))
mes2=int(input("mes\n"))
ano2=int(input("ano\n"))

if dia>dia2:
    print(dia, mes, ano, sep="/")
elif dia2<dia:
    print(dia2, mes2, ano2, sep="/")
elif mes>mes2:
    print(dia, mes, ano, sep="/")
elif mes2<mes:
    print(dia2, mes2, ano2, sep="/")
elif ano>ano:
    print(dia, mes, ano, sep="/")
else:
    print(dia2, mes2, ano2, sep="/")