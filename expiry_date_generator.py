import tkinter as tk
from datetime import datetime, timedelta


class ExpiryDateGenerator:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x250")  # Set window size to 400x250 pixels
        self.master.title("Expiry Date Generator")
        self.master.config(bg="#f5f5f5")  # Set background color to light gray

        # Label and Entry for production date
        self.prod_date_label = tk.Label(master, text="Production Date (DD/MM/YYYY):", bg="#f5f5f5")
        self.prod_date_label.pack(pady=10)
        self.prod_date_entry = tk.Entry(master)
        self.prod_date_entry.pack(pady=5)

        # Label and Entry for shelf life in days
        self.shelf_life_label = tk.Label(master, text="Shelf Life (in Days):", bg="#f5f5f5")
        self.shelf_life_label.pack()
        self.shelf_life_entry = tk.Entry(master)
        self.shelf_life_entry.pack(pady=5)

        # Button to generate expiry date
        self.generate_button = tk.Button(master, text="Generate Expiry Date", bg="#4CAF50", fg="white",
                                         command=self.generate_expiry_date)
        self.generate_button.pack(pady=10)

        # Label to display expiry date
        self.expiry_date_label = tk.Label(master, text="", bg="#f5f5f5")
        self.expiry_date_label.pack(pady=5)

    def generate_expiry_date(self):
        prod_date_str = self.prod_date_entry.get()
        shelf_life_str = self.shelf_life_entry.get()

        # Convert production date and shelf life to datetime objects
        prod_date = datetime.strptime(prod_date_str, '%d/%m/%Y')
        shelf_life = timedelta(days=int(shelf_life_str))

        # Calculate expiry date
        expiry_date = prod_date + shelf_life

        # Update label with expiry date
        self.expiry_date_label.config(text=f"Expiry Date: {expiry_date.strftime('%d/%m/%Y')}")


root = tk.Tk()
app = ExpiryDateGenerator(root)
root.mainloop()
