import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import PyPDF2
 
 
def select_pdf():
   global file_path
   file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
   if file_path:
       status_label.config(text="PDF selected: " + file_path, fg="blue")
       lock_button.config(state=tk.NORMAL)
   else:
       status_label.config(text="No file selected", fg="red")
 
 
def lock_pdf():
   password = simpledialog.askstring("Password", "Enter a password to lock the PDF:", show="*")
   if password:
       try:
           with open(file_path, 'rb') as file:
               pdf_reader = PyPDF2.PdfReader(file)
               pdf_writer = PyPDF2.PdfWriter()
               for page in pdf_reader.pages:
                   pdf_writer.add_page(page)
               pdf_writer.encrypt(password)
               output_path = file_path[:-4] + "_locked.pdf"
               with open(output_path, 'wb') as output_file:
                   pdf_writer.write(output_file)
           messagebox.showinfo("Success", "PDF has been locked successfully!")
       except Exception as e:
           messagebox.showerror("Error", str(e))
   else:
       messagebox.showwarning("Warning", "No password entered. PDF not locked.")
 
 
root = tk.Tk()
root.title("PDF Locker - The Pycodes")
root.geometry("400x200")
root.resizable(False,False)
 
 
# Create a label
label = tk.Label(root, text="Choose a PDF file to lock:")
label.pack(pady=10)
 
 
# Create a "Select PDF" button
select_button = tk.Button(root, text="Select PDF", command=select_pdf)
select_button.pack()
 
 
# Create a "Lock PDF" button
lock_button = tk.Button(root, text="Lock PDF", command=lock_pdf, state=tk.DISABLED)
lock_button.pack(pady=10)
 
 
# Status label
status_label = tk.Label(root, text="", fg="red")
status_label.pack(pady=10)
 
 
file_path = ""
 
 
root.mainloop()
