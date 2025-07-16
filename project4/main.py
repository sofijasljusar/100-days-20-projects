from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk, UnidentifiedImageError

BLUE = "#009EB7"
WATERMARK_SCALE = 0.2
WATERMARK_PADDING = 10


class WatermarkApp:
    """This app allows user to:
    1) upload image
    2) add png watermark (added to bottom right corner)
    3) download image (in original size with watermark)"""

    def __init__(self):
        self.window = Tk()

        self.image_canvas = None
        self.original_image = None
        self.watermark_image = None
        self.composited_original = None

        self.upload_button = None
        self.download_button = None
        self.watermark_button = None

        self.setup_ui()
        self.window.mainloop()

    def setup_ui(self):
        self.window.title("Add Watermark")
        self.window.attributes('-fullscreen', True)
        self.window.minsize(width=700, height=500)
        self.window.config(bg=BLUE, padx=50)

        for i in range(7):
            self.window.grid_rowconfigure(i, weight=1)

        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=8)

        self.upload_button = Button(
            text="Upload Image",
            highlightbackground=BLUE,
            height=2,
            width=15,
            command=self.upload_image
        )
        self.upload_button.grid(column=0, row=1)

        self.watermark_button = Button(
            text="Add Watermark",
            highlightbackground=BLUE,
            height=2,
            width=15,
            command=self.upload_watermark,
            state=DISABLED
        )
        self.watermark_button.grid(column=0, row=2)

        self.download_button = Button(
            text="Download Image",
            highlightbackground=BLUE,
            height=2,
            width=15,
            command=self.download_image,
            state=DISABLED
        )
        self.download_button.grid(column=0, row=3)

        self.image_canvas = Canvas(self.window, bg='white')
        self.image_canvas.grid(column=1, row=1, rowspan=5, sticky="nsew")

    def upload_image(self):
        try:
            filetypes = [("Image files", ("*.png", "*.jpg", "*.jpeg"))]
            path = askopenfilename(filetypes=filetypes)

            self.original_image = Image.open(path)

            self.image_canvas.config(bg="black")

            self.display_preview(self.original_image)

            self.watermark_button.config(state=NORMAL)

        except UnidentifiedImageError:
            messagebox.showinfo(title='Upload Error',
                                message='Image could not be read, please make sure the selected is an image file')

    def display_preview(self, image):
        """Displays passed image in resized version to fit canvas;
        stretches image to full width or height on canvas, based on whichever is bigger"""
        self.image_canvas.update_idletasks()  # Ensure canvas size is updated
        canvas_width = self.image_canvas.winfo_width()
        canvas_height = self.image_canvas.winfo_height()
        scale_w = canvas_width / image.width
        scale_h = canvas_height / image.height
        scale = min(scale_w, scale_h)
        new_w = int(image.width * scale)
        new_h = int(image.height * scale)
        preview = image.resize((new_w, new_h), Image.LANCZOS)

        img = ImageTk.PhotoImage(preview)
        self.image_canvas.delete("all")
        self.image_canvas.img = img
        self.image_canvas.create_image(canvas_width / 2, canvas_height / 2, image=img, anchor=CENTER)

    def upload_watermark(self):
        try:
            filetypes = [("PNG files", "*.png")]
            path = askopenfilename(filetypes=filetypes)

            self.watermark_image = Image.open(path).convert("RGBA")

            self.apply_watermark()

        except UnidentifiedImageError:
            messagebox.showinfo(title='Upload Error',
                                message='File could not be read. Please choose a valid PNG image.')

    def apply_watermark(self):
        base = self.original_image.convert("RGBA")
        watermark = self.watermark_image.copy()

        wm_width = int(base.width * WATERMARK_SCALE)
        scale = wm_width / watermark.width
        wm_height = int(watermark.height * scale)
        watermark = watermark.resize((wm_width, wm_height), Image.LANCZOS)

        position = (base.width - wm_width - WATERMARK_PADDING, base.height - wm_height - WATERMARK_PADDING)
        base.paste(watermark, position, watermark)

        self.composited_original = base.copy()

        self.display_preview(base)

        self.download_button.config(state=NORMAL)

    def download_image(self):
        path = asksaveasfilename(defaultextension=".png",
                                 filetypes=[("PNG files", "*.png")])
        if path:
            self.composited_original.save(path)
            messagebox.showinfo("Saved", f"Image saved to {path}")


if __name__ == "__main__":
    WatermarkApp()
