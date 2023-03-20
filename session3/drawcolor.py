from turtle import *
color=['red','blue','brown','green','purple','yellow','silver']
#       0       1       2       3       4       5       6

for conner in range(3,8):
    for edge in range(conner): 
        forward(100)
        left(360/conner)

mainloop()