import os
import sys
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from TextEditor import TextEditor
import tkinter.font as tkfont 


class EditorWindow:
    def __init__(self):
        self.editor = None
        self.window = tk.Tk()
        self.text = None
        self.scrollbar = None
        self.original_lines = 0
        self.next_button_disabled = False


        self.create_window()
        self.show_popup()



    def create_window(self):
        self.window.title("Writing Editor")
        self.window.geometry("700x400")
        self.current_font_size = 12

        # Set the desired font and size
        font = tkfont.Font(family="Arial", size=12)

         # Create a label for displaying the changing text
        self.display_text = tk.Label(
            self.window,
            text="",
            anchor=tk.CENTER,
            pady=10,
            fg="black"  # Set the text color to light gray
        )
        self.display_text.pack(side=tk.BOTTOM, fill=tk.X)

        self.prev_button = tk.Button(self.window, text="Prev", bg="dark blue", fg="white", command=self.prev_function)
        self.prev_button.pack(side=tk.LEFT, padx=5, pady=5)


        self.sub_button = tk.Button(self.window, text="Sub", bg="dark blue", fg="white", command=self.sub_function)
        self.sub_button.pack(side=tk.LEFT, padx=5, pady=5)


        self.add_button = tk.Button(self.window, text="Add", bg="dark blue", fg="white", command=self.add_function)
        self.add_button.pack(side=tk.RIGHT, padx=5, pady=5)


        self.next_button = tk.Button(self.window, text="Next", bg="dark blue", fg="white", command=self.next_function)
        self.next_button.pack(side=tk.RIGHT, padx=5, pady=5)

        button_frame = tk.Frame(self.window)
        button_frame.pack(side=tk.TOP, pady=5)


        self.past_button = tk.Button(button_frame, text="Show Past", bg="dark red", fg="white", command=self.past_function)
        self.past_button.pack(side=tk.LEFT, padx=5)


        self.all_button = tk.Button(button_frame, text="Show All", bg="dark red", fg="white", command=self.all_function)
        self.all_button.pack(side=tk.LEFT, padx=5)

        self.all_button = tk.Button(button_frame, text="+", bg="dark gray", fg="black", command=self.increase_text_function)
        self.all_button.pack(side=tk.LEFT, padx=5)

        self.all_button = tk.Button(button_frame, text="-", bg="dark gray", fg="black", command=self.decrease_text_function)
        self.all_button.pack(side=tk.LEFT, padx=5)


        self.scrollbar = tk.Scrollbar(self.window)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text = tk.Text(self.window, yscrollcommand=self.scrollbar.set, font=font)
        self.text.pack(fill=tk.BOTH, expand=True)

        self.scrollbar.config(command=self.text.yview)

        # The '<Key>' event is valled whenever any key is pressed in the text widget
        #self.text.bind('<Key>', self.save_file)  # Bind save_file to the Modified event


    def show_popup(self):
        num_paragraphs = simpledialog.askinteger("Number of Paragraphs", "Enter the number of paragraphs:")
        if num_paragraphs is not None:
            self.editor = TextEditor(num_paragraphs)
            text_content = self.editor.split_text()
            self.original_lines = len(self.editor.display)
            self.text.insert(tk.END, text_content)

            position = "[{}/{}]".format(self.editor.pos, len(self.editor.paragraphs)//self.editor.n + 1)
            self.display_text.config(text=position)


        # Check if the "Next" button should be initially disabled
        if self.next_button_disabled:
            self.next_button.config(state=tk.DISABLED)

    def increase_text_function(self):
        self.current_font_size += 2
        new_font = tkfont.Font(size=self.current_font_size)
        self.text.configure(font=new_font)

    def decrease_text_function(self):
        self.current_font_size -= 2
        new_font = tkfont.Font(size=self.current_font_size)
        self.text.configure(font=new_font)


    def prev_function(self):
        if self.editor.index < len(self.editor.paragraphs) and self.editor.index > self.original_lines:
            self.save_file()
        self.editor.reset_lines()
        self.text.delete('1.0', tk.END)
        text_content = self.editor.previous()
        self.text.insert(tk.END, text_content)
        self.original = text_content
        self.text.update()

        # Update the display_text label with the new text
        # Update the display_text label with the new text
        position = "[{}/{}]".format(self.editor.pos, len(self.editor.paragraphs)//self.editor.n + 1)
        self.display_text.config(text=position)

        # Check if the index is less than the total number of paragraphs
        if self.editor.index < len(self.editor.paragraphs):
            self.next_button.config(state=tk.NORMAL)  # Enable the "Next" button
            self.next_button_disabled = False

    def sub_function(self):
        self.save_file()
        self.text.delete('1.0', tk.END)
        text_content = self.editor.sub()
        self.text.insert(tk.END, text_content)
        self.original = text_content
        self.text.update()

        # Check if the index is less than the total number of paragraphs
        if self.editor.index < len(self.editor.paragraphs):
            self.next_button.config(state=tk.NORMAL)  # Enable the "Next" button
            self.next_button_disabled = False


    def add_function(self):
        self.save_file()
        self.text.delete('1.0', tk.END)
        text_content = self.editor.add()
        self.text.insert(tk.END, text_content)
        self.original = text_content
        self.text.update()


    def next_function(self):
        if self.editor.index < len(self.editor.paragraphs):
            self.save_file()
        self.editor.reset_lines()
        self.text.delete('1.0', tk.END)
        text_content = self.editor.next()
        self.text.insert(tk.END, text_content)
        self.original = text_content
        self.text.update()

        # Update the display_text label with the new text
        position = "[{}/{}]".format(self.editor.pos, len(self.editor.paragraphs)//self.editor.n + 1)
        self.display_text.config(text=position)

        # Check if the index has reached the end of paragraphs
        if self.editor.index >= len(self.editor.paragraphs):
            self.next_button.config(state=tk.DISABLED)  # Gray out the "Next" button
            self.next_button_disabled = True


    def past_function(self):
        self.text.delete('1.0', tk.END)
        text_content = self.editor.display_past()
        self.text.insert(tk.END, text_content)
        self.text.update()


    def all_function(self):
        self.text.delete('1.0', tk.END)
        text_content = self.editor.display_all()
        self.text.insert(tk.END, text_content)
        self.text.update()


    def generate_text(self, num_paragraphs):
        self.editor.split_text(num_paragraphs)

# IT's continously displaying the text, the next iteration of the text shown is complete edited one 
#Have to find a way to just display the edited text and replace all the old one
    def save_file(self, event=None):
        # Get the edited content from the Text widget
        edited_content = self.text.get('1.0', tk.END).split('\n\n')
        self.editor.save(edited_content, self.original_lines)

        # Create the new file content by joining the edited lines with newline characters
        new_file_content = '\n\n'.join(self.editor.paragraphs)

        try:
            with open("Edited_File.txt", 'w', encoding="utf-8", buffering=1) as file:
                file.write(new_file_content)
        except IOError:
            messagebox.showinfo("Failed", "File can't be saved. Try again.")

    def run(self):
        self.window.mainloop()

# Create an instance of the EditorWindow class
editor = EditorWindow()
editor.run()


