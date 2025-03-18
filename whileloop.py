import turtle 

def draw_square()
    ("for_in range (4)")
    turtle.forward(30)
    turtle.right(90)
 
def on_key_pressed():
    draw_square()
    turtle.listen()
    turtle.onkey(on_key_pressed, "space")
turtle.mainloop()