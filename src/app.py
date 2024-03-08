import tensorflow as tf
import tkinter as tk
import customtkinter as ctk

from PIL import ImageTk
from authtoken import auth_token

import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

# Create the app
app = tk.Tk()
app.geometry("532x622")
app.title("Aurora Ignite")
ctk.set_appearance_mode("dark")

prompt = ctk.CTkEntry(master=app, height=40, width=512, text_color="black", fg_color="white")
prompt.place(x=10, y=10)
prompt.configure(font=("Arial", 20))

lmain = ctk.CTkLabel(master=app, height=512, width=512)
lmain.place(x=10, y=110)

modelid = "CompVis/stable-diffusion-v1-4"

device = 'cuda' if tf.config.list_physical_devices('GPU') else 'cpu'
# device = "cuda"

pipe = StableDiffusionPipeline.from_pretrained(modelid, revision="fp16", torch_dtype=torch.float32, use_auth_token=auth_token)
pipe.to(device)

def generate():
    with autocast(device):
        result = pipe(prompt.get(), guidance_scale=8.5)
        image = result.images[0]  

    image.save('generatedImage.png')
    img = ImageTk.PhotoImage(image)
    lmain.configure(image=img)

trigger = ctk.CTkButton(master=app, height=40, width=120, text_color="white", fg_color="blue", command=generate)
trigger.configure(font=("Arial", 20), text="Generate")
trigger.place(x=206, y=60)

app.mainloop()