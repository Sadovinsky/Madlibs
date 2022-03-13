"""
Program, który tworzy krótką opowieść na podstawie podanych zmiennych
"""
kto = input("wymień osobę : ")
co = input("napisz co robi: " )
rodzina = input("podaj członka rodziny : ")
przysłowie = input ("podaj przysłowie :")
madlib = f"Podobno {kto}, ciągle {co} ponieważ w dzieciństwie jego {rodzina} powtarzał:  {przysłowie} "
print(madlib)