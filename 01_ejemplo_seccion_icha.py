from secciones import SeccionICHA

sec1 = SeccionICHA("H1100x350x400.4",base_datos="Perfiles ICHA.xlsx")
print(sec1)

sec2 = SeccionICHA("H1100x350x400.",base_datos="Perfiles ICHA.xlsx")
print(sec2)

sec3 = SeccionICHA("HR1118x405x517.7",base_datos="Perfiles ICHA.xlsx")
print(sec3)
