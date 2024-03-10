import tkinter as tk
from PIL import ImageTk, Image
import glob
from tkinterhtml import HtmlFrame

class ImageViewer:
    def __init__(self, master, image_paths, video_url):
        self.master = master
        self.image_paths = image_paths
        self.current_image_index = 0

        # Load initial image
        try:
            self.load_image()
        except Exception as e:
            print("Error loading initial image:", e)
            self.master.destroy()
            return

        # Create image label
        self.image_label = tk.Label(master, image=self.tk_image)
        self.image_label.place(x=0, y=master.winfo_screenheight() - 512)  # Place image at the bottom left corner

        # Schedule image change every 5 seconds
        self.master.after(5000, self.change_image)

        # Embed YouTube video
        self.video_frame = HtmlFrame(master)
        self.video_frame.set_content(f'<iframe width="420" height="315" src="{video_url}"></iframe>')
        self.video_frame.place(x=master.winfo_screenwidth() - 420, y=20)  # Place video at the top right corner

    def load_image(self):
        image_path = self.image_paths[self.current_image_index]
        image = Image.open(image_path)
        image = image.resize((512, 512))
        self.tk_image = ImageTk.PhotoImage(image)

    def change_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
        try:
            self.load_image()
        except Exception as e:
            print("Error loading image:", e)
            self.master.destroy()
            return
        self.image_label.configure(image=self.tk_image)

        # Schedule the next image change
        self.master.after(5000, self.change_image)

if __name__ == "__main__":
    # Get list of image file paths using glob
    image_paths = glob.glob("out/*.png")  # Change the directory and file extension as needed

    if not image_paths:
        print("No images found in the specified directory.")
    else:
        # Specify the YouTube video URL
        video_url = "https://www.youtube.com/embed/T_KrYLW4jw8&list=PLzMcBGfZo4-nyLTlSRBvo0zjSnCnqjHYQ&ab_channel=TechWithTim"  # Replace "your-video-id" with the actual video ID

        # Create the app
        app = tk.Tk()
        app.geometry(f"{app.winfo_screenwidth()}x{app.winfo_screenheight()}")
        app.title("Image Viewer")

        # Create the image viewer
        image_viewer = ImageViewer(app, image_paths, video_url)

        app.mainloop()
