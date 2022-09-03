# importing libraries
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import filedialog

# defining main window
root = Tk()
root.title("Image Viewer App")
#root.iconbitmap('Images/Icon.ico')
root.state("zoomed")
root.configure(bg = "black")

#defining frame
frame = LabelFrame(root, padx = 20, pady = 20, bg = "orange")
frame.pack(padx = 20, pady = 20)

#defining app header
heading = Label(frame, text = "IMAGE VIEWER APP", bg = "orange")
heading.configure(font = ('Times',50, "bold"))
heading.grid(row = 0, column = 0, columnspan = 3, padx = 40, pady = 40)

#defining button hover functions
def on_enter(e):
   click_to_open.config(background='blue', foreground= "white")

def on_leave(e):
   click_to_open.config(background= 'white', foreground= 'black')

def on_enter2(e):
   click_to_view.config(background='blue', foreground= "white")

def on_leave2(e):
   click_to_view.config(background= 'white', foreground= 'black')

#defining variables for images
length = 0
img_list = []
image_list = []

#defining function to load images
def on_click():
	global length
	global img_list
	global image_list
	global status
	status.grid_forget()
	status = Label(frame, text = "LOADING IMAGES....", padx = 20, pady = 20, bg = "orange", fg = "red")
	status.configure(font = ("bold", 20))
	status.grid(row = 3, column = 1, padx = 20, pady = 20)
	img_list = []
	image_list = []
	root.filename = filedialog.askopenfilenames(initialdir = "/users/Aman Jain/PythonCourse/GUI/Image Viewer Dynamic App/Images", title="Select Images", filetypes = (("Jpg", "*.jpg"),) )
	length = len(root.filename)
	for x in range(length):
		img_list.append(root.filename[x])
	for x in range(length):
		img = Image.open(img_list[x])
		image = img.resize((600, 466), Image.ANTIALIAS)
		img = ImageTk.PhotoImage(image)
		image_list.append(img)
		
	status.grid_forget()
	status = Label(frame, text = "LOADED SUCCESSFULLY", padx = 20, pady = 20, bg = "orange", fg = "green")
	status.configure(font = ("bold", 20))
	status.grid(row = 3, column = 1, padx = 20, pady = 20)

#defining function to view images in a new window
def on_view():
	global label
	global prev_
	global next_
	global name
	#defining new window
	new_window = Toplevel(root)
	new_window.title("Images")
	#new_window.iconbitmap('Images/Icon.ico')
	new_window.state("zoomed")

	new_window.configure(bg = "black")

	frame1 = LabelFrame(new_window, padx = 20, pady = 20, bg = "orange")
	frame1.pack(padx = 20, pady = 20)

	# defining functions
	def next_image(image_number):
		global label
		global prev_
		global next_
		label.grid_forget()
		label = Label(frame1, image = image_list[image_number-1])
		label.grid(row = 1, column = 1)
		prev_ = Button(frame1, text = "<<",bg = "white", fg = "black", borderwidth = 5, padx = 20, pady = 20, command = lambda : prev_image(image_number-1))
		prev_.configure(font = (20))
		next_ = Button(frame1, text = ">>",bg = "white", fg = "black", borderwidth = 5, padx = 20, pady = 20, command = lambda : next_image(image_number+1))
		next_.configure(font = (20))
		prev_.grid(row = 1, column = 0, padx = 20, pady = 20)
		next_.grid(row = 1, column = 2, padx = 20, pady = 20)
		status_bar = Label(frame1, text = "Image " + str(image_number) + " of " + str(length), bd = 2, relief = SUNKEN, padx = 5, pady = 5, bg = "black", fg = "white")
		status_bar.configure(font=("bold", 20))
		status_bar.grid(row = 0, column = 1, sticky = W + E, padx = 10, pady = 10)
		if image_number == length:
			next_ = Button(frame1, text = ">>",bg = "white", fg = "black", borderwidth = 5, padx = 20, pady = 20, state = DISABLED)
			next_.configure(font = (20))
			next_.grid(row = 1, column = 2, padx = 20, pady = 20)

	def prev_image(image_number):
		global label
		global prev_
		global next_
		label.grid_forget()
		label = Label(frame1, image = image_list[image_number-1])
		label.grid(row = 1, column = 1)
		prev_ = Button(frame1, text = "<<",bg = "white", fg = "black", borderwidth = 5, padx = 20, pady = 20, command = lambda : prev_image(image_number-1))
		prev_.configure(font = (20))
		next_ = Button(frame1, text = ">>",bg = "white", fg = "black", borderwidth = 5, padx = 20, pady = 20, command = lambda : next_image(image_number+1))
		next_.configure(font = (20))
		prev_.grid(row = 1, column = 0, padx = 20, pady = 20)
		next_.grid(row = 1, column = 2, padx = 20, pady = 20)
		status_bar = Label(frame1, text = "Image " + str(image_number) + " of " + str(length), bd = 2, relief = SUNKEN, padx = 5, pady = 5, bg = "black", fg = "white")
		status_bar.configure(font=("bold", 20))
		status_bar.grid(row = 0, column = 1, sticky = W + E, padx = 10, pady = 10)
		if image_number == 1:
			prev_ = Button(frame1, text = "<<",bg = "white", fg = "black", borderwidth = 5, padx = 20, pady = 20, state = DISABLED)
			prev_.configure(font = (20))
			prev_.grid(row = 1, column = 0, padx = 20, pady = 20)

	# defining display of second window
	status_bar = Label(frame1, text = "Image 1 of " + str(length), bd = 2, relief = SUNKEN, padx = 5, pady = 5, bg = "black", fg = "white")
	status_bar.configure(font=("bold", 20))
	status_bar.grid(row = 0, column = 1, sticky = W + E, padx = 10, pady = 10)

	prev_ = Button(frame1, text = "<<",bg = "white", fg = "black", borderwidth = 5, padx = 20, pady = 20, command = lambda : prev_image(), state = DISABLED)
	prev_.configure(font = (20))
	next_ = Button(frame1, text = ">>",bg = "white", fg = "black", borderwidth = 5, padx = 20, pady = 20, command = lambda : next_image(2))
	next_.configure(font = (20))
	prev_.grid(row = 1, column = 0, padx = 20, pady = 20)
	next_.grid(row = 1, column = 2, padx = 20, pady = 20)

	label = Label(frame1, image = image_list[0])
	label.grid(row = 1, column = 1)

	fullscreen = Button(frame1, text = "FULLSCREEN IMAGE",padx = 20, pady = 20)
	fullscreen.grid(row = 2, column = 1, padx = 20, pady = 20)



	
# defining display of main window
click_to_open = Button(frame, text = "Click to open images", bg = "white", fg = "black", padx = 10, pady = 10, borderwidth = 5, command = on_click)
click_to_open.configure(font=(25))
click_to_open.grid(row = 1, column = 0, columnspan = 3, padx = 20, pady = 20)

click_to_open.bind('<Enter>', on_enter)
click_to_open.bind('<Leave>', on_leave)

click_to_view = Button(frame, text = "Click to view selected images", bg = "white", fg = "black", padx = 10, pady = 10, borderwidth = 5, command = on_view)
click_to_view.configure(font=(25))
click_to_view.grid(row = 2, column = 0, columnspan = 3, padx = 20, pady = 20)

click_to_view.bind('<Enter>', on_enter2)
click_to_view.bind('<Leave>', on_leave2)

status = Label(frame, text = " ", padx = 20, pady = 20, bg = "orange", fg = "white")
status.configure(font = ("bold", 20))
status.grid(row = 3, column = 0, columnspan = 3, padx = 20, pady = 20)

# mainloop which run infinitely
root.mainloop()