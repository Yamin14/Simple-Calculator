from tkinter import *
root = Tk()
bg = "sky blue"
fg = "blue"
acbg = "cyan"
ff = ("Comic Sans MS", 20)
ff1 =  ("Comic Sans MS", 14)
fbg = "turquoise"
root.config(background=bg)
class Calc():
	def __init__(self, text):
		self.text = text
		
ans = Calc("")
input = Calc("")

def buttonfunc(b):
	if b['text'] == "Clear":
		inputlbl['text'] = ""
		anslbl['text'] = ""
		
	elif b['text'] == " Del ":
		inputlbl['text'] = inputlbl['text'][:-1]

	elif b['text'] == " . ":
		inputlbl['text'] += "."
		
	elif b['text'] == "=":
		anslbl['text'] = eval(inputlbl['text'])

	else:
		inputlbl['text'] += b['text']

topframe = Frame(root, bg=fbg, padx=200)
midframe = Frame(root, bg=bg)
bottomframe = Frame(root, bg=bg)

topframe.pack()
midframe.pack()
bottomframe.pack()

inputlbl = Label(topframe, text=input.text, font=ff1, bg=fbg, fg=fg)
inputlbl.grid(row=0,column=0)

exline = Label(topframe, text="      ", font=ff1, bg=fbg, fg=fg)
exline.grid(row=1,column=0)

anslbl = Label(topframe, text=ans.text, font=ff1, bg=fbg, fg=fg)
anslbl.grid(row=2,column=0)

bcl = Button(midframe, text="Clear", bg=bg, fg=fg, activebackground=acbg, font=ff1)
bdel = Button(midframe, text=" Del ", bg=bg, fg=fg, activebackground=acbg, font=ff1)

bcl.grid(row=0, column=0)
bdel.grid(row=0, column=1)

b1 = Button(bottomframe, text="1", bg=bg, fg=fg, activebackground=acbg, font=ff)
b2 = Button(bottomframe, text="2", bg=bg, fg=fg, activebackground=acbg , font=ff)
b3 = Button(bottomframe, text="3", bg=bg, fg=fg, activebackground=acbg, font=ff)
b4 = Button(bottomframe, text="4", bg=bg, fg=fg, activebackground=acbg, font=ff)
b5 = Button(bottomframe, text="5", bg=bg, fg=fg, activebackground=acbg, font=ff)
b6 = Button(bottomframe, text="6", bg=bg, fg=fg, activebackground=acbg, font=ff)
b7 = Button(bottomframe, text="7", bg=bg, fg=fg, activebackground=acbg, font=ff)
b8 = Button(bottomframe, text="8", bg=bg, fg=fg, activebackground=acbg, font=ff)
b9 = Button(bottomframe, text="9", bg=bg, fg=fg, activebackground=acbg, font=ff)
b0 = Button(bottomframe, text="0", bg=bg, fg=fg, activebackground=acbg, font=ff)
bp = Button(bottomframe, text=" . ", bg=bg, fg=fg, activebackground=acbg, font=ff, padx=25)
be = Button(bottomframe, text="=", bg=bg, fg=fg, activebackground=acbg, font=ff)

bpl = Button(bottomframe, text="+", bg=bg, fg=fg, activebackground=acbg, font=ff1, padx=40, pady=33)
bmi = Button(bottomframe, text="-", bg=bg, fg=fg, activebackground=acbg, font=ff1, padx=45, pady=33)
bmu = Button(bottomframe, text="*", bg=bg, fg=fg, activebackground=acbg, font=ff1, padx=40, pady=33)
bdi = Button(bottomframe, text="/", bg=bg, fg=fg, activebackground=acbg, font=ff1, padx=42, pady=33)

b1.grid(row=2, column=0)
b2.grid(row=2, column=1)
b3.grid(row=2, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=0, column=0)
b8.grid(row=0, column=1)
b9.grid(row=0, column=2)
b0.grid(row=3, column=1)
bp.grid(row=3, column=0)
be.grid(row=3, column=2)
bdi.grid(row=3, column=3)
bmu.grid(row=2, column=3)
bmi.grid(row=1, column=3)
bpl.grid(row=0, column=3)

b1['command'] = lambda b=b1: buttonfunc(b)
b2['command'] = lambda b=b2: buttonfunc(b)
b3['command'] = lambda b=b3: buttonfunc(b)
b4['command'] = lambda b=b4: buttonfunc(b)
b5['command'] = lambda b=b5: buttonfunc(b)
b6['command'] = lambda b=b6: buttonfunc(b)
b7['command'] = lambda b=b7: buttonfunc(b)
b8['command'] = lambda b=b8: buttonfunc(b)
b9['command'] = lambda b=b9: buttonfunc(b)
b0['command'] = lambda b=b0: buttonfunc(b)
bpl['command'] = lambda b=bpl: buttonfunc(b)
bp['command'] = lambda b=bp: buttonfunc(b)
be['command'] = lambda b=be: buttonfunc(b)
bcl['command'] = lambda b=bcl: buttonfunc(b)
bdel['command'] = lambda b=bdel: buttonfunc(b)
bmi['command'] = lambda b=bmi: buttonfunc(b)
bmu['command'] = lambda b=bmu: buttonfunc(b)
bdi['command'] = lambda b=bdi: buttonfunc(b)

root.mainloop()
