from turtle import *
color_list = [
    'red', # 3
    'blue', 
    'yellow', 
    'green', 
    'gray', 
    'purple', 
    'brown'
]

for color_index in range(len(color_list)):
    color(color_list[color_index])
    for j in range(color_index + 3):
        forward(100)
        left(360/(color_index + 3))
for i in range(len(color_list)):
    color(color_list[i])


pencolor('white')
back(100)
right(90)
forward(200)
left(90)
forward(200)
pencolor('red')
left(90)
forward(100)
left(90)
forward(200)
left(90)
forward(100)
left(90)
forward(200)

mainloop()