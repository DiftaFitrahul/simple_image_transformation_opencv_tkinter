import cv2
import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
import numpy as np

# Create a Tkinter window
root = tk.Tk()
root.geometry('900x600')
root.title("Image Translation")

# initial position of image
current_translation = np.float32([[1,0,0],[0,1,0],[0,0,1]])

# translation matrix with x = 450, y = 150
translation_transformation = np.float32([[1,0,450],[0,1,150],[0,0,1]])

# rotation matrix with 45 degree
rotation_transformation = np.float32([[0.707,-0.707,0],[0.707,0.707,0],[0,0,1]])

# scaling matrix with y = 2 times 
scaling_transformation = np.float32([[1,0,0],[0,2,0],[0,0,1]])

# define global variable
global image_object, image_loaded

def initial_image():
    global image_object, image_loaded, current_translation, image

    #specify a file that can be uploaded to the program, in this case it is only png, jpg, and jpeg file 
    f_types = [('image files', '*.png;*.jpg;*.jpeg')]

    # open the directory
    filepath = askopenfilename(filetypes= f_types)

    image = cv2.imread(filepath)

    translated_image = cv2.warpPerspective(image, current_translation, (image.shape[1]+500, image.shape[0]+500))
    
    # Convert the OpenCV image to a PIL image
    pil_image = Image.fromarray(cv2.cvtColor(translated_image, cv2.COLOR_BGR2RGB))

    pil_image = pil_image.resize((500,400), Image.LANCZOS)
    photo_image = ImageTk.PhotoImage(pil_image)
    label.config(image= photo_image)
    label.image = photo_image


def first_transformation():
    global translation_transformation, image
    
    
    # make a first transformation by use translation_tranformation
    translated_image = cv2.warpPerspective(image, translation_transformation, (image.shape[1]+500, image.shape[0]+500))
    
    # Convert the OpenCV image to a PIL image
    pil_image = Image.fromarray(cv2.cvtColor(translated_image, cv2.COLOR_BGR2RGB))
    
    # Resize the PIL image to fit on the Tkinter window
    pil_image = pil_image.resize((500, 400), Image.LANCZOS)
    
    # Convert the PIL image to a Tkinter PhotoImage
    photo_image = ImageTk.PhotoImage(pil_image)
    
    # Display the PhotoImage on the Tkinter window
    label.config(image=photo_image)
    label.image = photo_image

def second_transformation():
    global translation_transformation, rotation_transformation, image

    # multiply translation_transformation and rotation_transformation for the next transformation
    combine_transformation = np.dot(translation_transformation, rotation_transformation)

    # use second_transformation
    translated_image = cv2.warpPerspective(image, combine_transformation, (image.shape[1]+500, image.shape[0]+500))
    
    # Convert the OpenCV image to a PIL image
    pil_image = Image.fromarray(cv2.cvtColor(translated_image, cv2.COLOR_BGR2RGB))
    
    # Resize the PIL image to fit on the Tkinter window
    pil_image = pil_image.resize((500, 400), Image.LANCZOS)
    
    # Convert the PIL image to a Tkinter PhotoImage
    photo_image = ImageTk.PhotoImage(pil_image)
    
    # Display the PhotoImage on the Tkinter window
    label.config(image=photo_image)
    label.image = photo_image

def thrid_transformation():
    global translation_transformation, rotation_transformation, image, scaling_transformation

    # multiply translation_transformation with rotation transformation
    combined_transformation = np.dot(translation_transformation, rotation_transformation)

    # result of the translation transformation multipy with rotation transformation we multiply again with scaling transformation
    combined_transformation = np.dot(combined_transformation, scaling_transformation)
    
    
    
    translated_image = cv2.warpPerspective(image, combined_transformation, (image.shape[1]+500, image.shape[0]+500))
    
    # Convert the OpenCV image to a PIL image
    pil_image = Image.fromarray(cv2.cvtColor(translated_image, cv2.COLOR_BGR2RGB))
    
    # Resize the PIL image to fit on the Tkinter window
    pil_image = pil_image.resize((500, 400), Image.LANCZOS)
    
    # Convert the PIL image to a Tkinter PhotoImage
    photo_image = ImageTk.PhotoImage(pil_image)
    
    # Display the PhotoImage on the Tkinter window
    label.config(image=photo_image)
    label.image = photo_image

# Create a button to load an image and translation, rotation the image, and 

load_button = tk.Button(root, text="Load Image", command=initial_image, font= ('times', 18, 'bold'))
load2_button = tk.Button(root, text="translation x = 450, y = 150", command=first_transformation)
load3_button = tk.Button(root, text="translation x = 450, y = 150 + rotation 45 derajat", command=second_transformation)
load4_button = tk.Button(root, text="translation x = 450, y = 150 + rotation 45 derajat + scale y = 2x", command=thrid_transformation)

load_button.pack()
load2_button.pack()
load3_button.pack()
load4_button.pack()

# Create a label to display the image
label = tk.Label(root)
label.pack()

# Start the Tkinter event loop
root.mainloop()
