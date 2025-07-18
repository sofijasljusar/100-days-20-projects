from tkinter import *
from tkinter import messagebox

PINK = "#FFC3E9"
GREY = "#B7B7B7"


class TypingSpeedTest:

    def __init__(self):
        self.window = Tk()

        self.practice_text = (
            "When I am an old woman I shall wear purple. "
            "With a red hat which doesn't go, and doesn't suit me. "
            "And I shall spend my pension on brandy and summer gloves. "
            "And satin sandals, and say we've no money for butter. "
            "I shall sit down on the pavement when I'm tired. "
            "And gobble up samples in shops and press alarm bells. "
            "And run my stick along the public railings. "
            "And make up for the sobriety of my youth. "
            "I shall go out in my slippers in the rain. "
            "And pick the flowers in other people's gardens. "
            "And learn to spit."
        )

        self.setup_ui()
        self.window.mainloop()

    def setup_ui(self):
        self.window.title("Typing Speed Test")
        self.window.attributes('-fullscreen', True)
        self.window.minsize(width=700, height=500)
        self.window.config(bg=PINK, padx=50, pady=50)

        self.window.grid_columnconfigure(0, weight=1)

        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=2)
        self.window.grid_columnconfigure(2, weight=1)

        self.window.grid_rowconfigure(0, weight=3)
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_rowconfigure(2, weight=3)

        self.start_button = Button(
            text="Start",
            highlightbackground=PINK,
            background="white",
            height=2,
            width=15,
            command=self.start_test
        )
        self.start_button.grid(column=1, row=1)

    def start_test(self):
        self.start_button.destroy()

        self.text_label = Text(
            font=("Helvetica", 16),
            background="white",
            foreground=GREY,
            wrap="word",
            highlightthickness=2,
            highlightbackground="black",
            highlightcolor="black",
            padx=20,
            pady=20
        )
        self.text_label.insert("1.0", self.practice_text)
        self.text_label.config(state="disabled")

        self.text_label.grid(column=1,
                             row=0,
                             sticky="nsew",
                             padx=100,
                             pady=(10, 5))

        self.input_field = Text(
            font=("Helvetica", 16),
            background="white",
            wrap="word",
            highlightthickness=2,
            highlightbackground="black",
            highlightcolor="black",
            padx=20,
            pady=20
        )
        self.input_field.grid(column=1,
                              row=2,
                              sticky="nsew",
                              padx=100,
                              pady=30)

        # start test
        self.input_field.bind("<KeyRelease>", self.check_input)

        self.window.after(60000, self.show_result)

    def check_input(self, event=None):
        typed_text = self.input_field.get("1.0", "end-1c")

        self.text_label.config(state="normal")

        # remove previous tags
        self.text_label.tag_remove("correct", "1.0", "end")
        self.text_label.tag_remove("incorrect", "1.0", "end")

        # reapply tags accordingly
        for i, char in enumerate(typed_text):
            if i < len(self.practice_text) and char == self.practice_text[i]:
                start_index = f"1.{i}"
                end_index = f"1.{i + 1}"
                self.text_label.tag_add("correct", start_index, end_index)
                self.text_label.tag_configure("correct", foreground="black")
            elif i < len(self.practice_text) and char != self.practice_text[i]:
                start_index = f"1.{i}"
                end_index = f"1.{i + 1}"
                self.text_label.tag_add("incorrect", start_index, end_index)
                self.text_label.tag_configure("incorrect", foreground="red")

        self.text_label.config(state="disabled")

    def calculate_correct_keys(self):
        ranges = self.text_label.tag_ranges("correct")
        correct_chars = 0

        for i in range(0, len(ranges), 2):
            start = ranges[i]
            end = ranges[i + 1]
            correct_chars += int(str(self.text_label.count(start, end, "chars")[0]))

        return correct_chars

    def show_result(self):
        chars_per_minute = self.calculate_correct_keys()
        messagebox.showinfo(title='Your Result',
                            message=f'{chars_per_minute} characters per minute')


if __name__ == "__main__":
    TypingSpeedTest()
