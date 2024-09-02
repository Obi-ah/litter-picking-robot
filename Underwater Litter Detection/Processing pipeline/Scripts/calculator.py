pix_x = 186 #
pix_y = 96 #

s_x = 129 - pix_x
s_y = 129 - pix_y

f = 335.1517

a = (f**2 + s_x**2)**0.5
f_o = (a**2 + s_y**2)**0.5

dist = 18.54822 #

X = dist * (s_x/f_o)
Y = dist * (s_y/f_o)
Z = dist * (f/f_o)


print(X,Y,Z)