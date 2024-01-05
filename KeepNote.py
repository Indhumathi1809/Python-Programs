import tkinter as tk
from tkinter import scrolledtext

class KeepNoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Keep Note App")

        # Entry widget for note input
        self.note_entry = scrolledtext.ScrolledText(root, width=40, height=10, wrap=tk.WORD)
        self.note_entry.pack(pady=10)

        # Button to save note
        tk.Button(root, text="Save Note", command=self.save_note).pack(pady=5)

        # Text widget to display saved notes
        self.display_area = scrolledtext.ScrolledText(root, width=40, height=10, wrap=tk.WORD)
        self.display_area.pack(pady=10)

    def save_note(self):
        note_text = self.note_entry.get("1.0", tk.END).strip()
        
        if note_text:
            # Save the note to the display area
            self.display_area.insert(tk.END, f"- {note_text}\n")

            # Clear the note entry
            self.note_entry.delete("1.0", tk.END)
        else:
            tk.messagebox.showwarning("Empty Note", "Please enter a note before saving.")

if __name__ == "__main__":
    root = tk.Tk()
    app = KeepNoteApp(root)
    root.mainloop()
