# bounce.py
#
# Exercise 1.5

height=100
rebote=3/5

for i in range(10):
    altura=height*rebote
    print ("Rebote",i,": ", round(altura,2))
    height=height*rebote