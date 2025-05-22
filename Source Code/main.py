import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import PhotoImage
from employees import Employee
from stock import Inventory, Item

class CashierApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ASISOFT SALES APP")
        self.geometry("710x500")
        self.resizable(True, True)

        # Uygulama küçük ikon
        icon = PhotoImage(file="logo.png")
        self.iconphoto(True, icon)

        #Kasiyer envanter deneme
        self.employees = [
            Employee("a", "1"),
            Employee("ayse", "5678"),
        ]
        self.inventory = Inventory()
        self.inventory.add_product(Item("Elma", 5.0, 50))
        self.inventory.add_product(Item("Armut", 6.0, 40))
        self.inventory.add_product(Item("Muz", 7.0, 30))

        self.current_employee = None

        self.login_frame = None
        self.signup_frame = None
        self.main_frame = None


        self.create_login_frame()

    #Login Ekranı
    def create_login_frame(self):
        if self.signup_frame:
            self.signup_frame.destroy()
            self.signup_frame = None
        if self.main_frame:
            self.main_frame.destroy()
            self.main_frame = None
        if self.login_frame:
            self.login_frame.destroy()
        self.login_frame = ttk.Frame(self)
        self.login_frame.pack(pady=80)

        ttk.Label(self.login_frame, text="Cashier Login", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(self.login_frame, text="Name:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.name_entry = ttk.Entry(self.login_frame)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.login_frame, text="Password:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.password_entry = ttk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=2, column=1, padx=5, pady=5)

        login_btn = ttk.Button(self.login_frame, text="Sign in", command=self.handle_login)
        login_btn.grid(row=3, column=0, columnspan=2, pady=15)

        signup_btn = ttk.Button(self.login_frame, text="Sign up", command=self.create_signup_frame)
        signup_btn.grid(row=4, column=0, columnspan=2, pady=5)

    #Kasiyer kayıt
    def create_signup_frame(self):
        if self.login_frame:
            self.login_frame.destroy()
            self.login_frame = None
        if self.signup_frame:
            self.signup_frame.destroy()
        self.signup_frame = ttk.Frame(self)
        self.signup_frame.pack(pady=80)

        ttk.Label(self.signup_frame, text="Sign up", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(self.signup_frame, text="Name:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.signup_name_entry = ttk.Entry(self.signup_frame)
        self.signup_name_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.signup_frame, text="Password:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.signup_password_entry = ttk.Entry(self.signup_frame, show="*")
        self.signup_password_entry.grid(row=2, column=1, padx=5, pady=5)

        signup_btn = ttk.Button(self.signup_frame, text="Sign up", command=self.handle_signup)
        signup_btn.grid(row=3, column=0, columnspan=2, pady=15)

        back_btn = ttk.Button(self.signup_frame, text="Back to Login", command=self.create_login_frame)
        back_btn.grid(row=4, column=0, columnspan=2, pady=5)

    #Kayıt olma
    def handle_signup(self):
        name = self.signup_name_entry.get().strip()
        password = self.signup_password_entry.get().strip()

        if not name or not password:
            messagebox.showerror("Error", "Name and Password cannot be blank.")
            return

        if self.get_employee_by_name(name):
            messagebox.showerror("Error", "This name have already exist.")
            return

        new_employee = Employee(name, password)
        self.employees.append(new_employee)
        messagebox.showinfo("Succesful", f"Registiration Succesful! Welcome {name}!")
        self.create_login_frame()

    def get_employee_by_name(self, name):
        for emp in self.employees:
            if emp.name == name:
                return emp
        return None

    #Giriş yapma
    def handle_login(self):
        name = self.name_entry.get().strip()
        password = self.password_entry.get().strip()
        for emp in self.employees:
            if emp.check_password(name, password):
                self.current_employee = emp
                messagebox.showinfo("Succesful", f"Welcome {name}!")
                self.login_frame.destroy()
                self.login_frame = None
                self.create_main_frame()
                return
        messagebox.showerror("Error", "Name or Password is incorrect. Please Try Again.")

    #Ana ekran UI
    def create_main_frame(self):
        if self.login_frame:
            self.login_frame.destroy()
            self.login_frame = None
        if self.signup_frame:
            self.signup_frame.destroy()
            self.signup_frame = None
        if self.main_frame:
            self.main_frame.destroy()
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=1, pady=1)

        # Hoşgeldin Label
        ttk.Label(self.main_frame, text=f"\tWelcome {self.current_employee.name}", font=("Arial", 14, "bold")).grid(row=0, column=1, columnspan=3, pady=10)

        # Çıkış yapma
        logout_btn = ttk.Button(self.main_frame, text="Exit", command=self.logout)
        logout_btn.grid(row=10, column=6, padx=5, pady=10)

        # Satış
        ttk.Label(self.main_frame, text="Sales Product Name:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.sale_product_entry = ttk.Entry(self.main_frame)
        self.sale_product_entry.grid(row=1, column=1, pady=5)
        ttk.Label(self.main_frame, text="Quantity:").grid(row=1, column=2, sticky=tk.W, pady=5)
        self.sale_qty_entry = ttk.Entry(self.main_frame, width=5)
        self.sale_qty_entry.grid(row=1, column=3, pady=5)
        self.sale_button = ttk.Button(self.main_frame, text="Sell Stock", command=self.handle_sale)
        self.sale_button.grid(row=1, column=4, padx=5, pady=5)

        # Stok ekleme
        ttk.Label(self.main_frame, text="Product of Adding Stock:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.stock_product_entry = ttk.Entry(self.main_frame)
        self.stock_product_entry.grid(row=2, column=1, pady=5)
        ttk.Label(self.main_frame, text="Quantity:").grid(row=2, column=2, sticky=tk.W, pady=5)
        self.stock_qty_entry = ttk.Entry(self.main_frame, width=5)
        self.stock_qty_entry.grid(row=2, column=3, pady=5)
        self.stock_add_button = ttk.Button(self.main_frame, text="Add Stock", command=self.handle_stock_add)
        self.stock_add_button.grid(row=2, column=4, padx=5, pady=5)

        # Ürün listeleme
        self.list_button = ttk.Button(self.main_frame, text="Show the Stock List", command=self.show_inventory)
        self.list_button.grid(row=3, column=0, pady=10, sticky=tk.W)

        # Günlük işlem sayısı
        self.tx_count_button = ttk.Button(self.main_frame, text="Show Daily Transaction Count", command=self.show_transaction_count)
        self.tx_count_button.grid(row=3, column=1, pady=10, sticky=tk.W)

        # Yeni ürün ekleme
        ttk.Label(self.main_frame, text="New Product:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.new_product_name_entry = ttk.Entry(self.main_frame)
        self.new_product_name_entry.grid(row=4, column=1, pady=5)

        ttk.Label(self.main_frame, text="Price:").grid(row=4, column=2, sticky=tk.W, pady=5)
        self.new_product_price_entry = ttk.Entry(self.main_frame, width=10)
        self.new_product_price_entry.grid(row=4, column=3, pady=5)

        ttk.Label(self.main_frame, text="\tStock:").grid(row=4, column=4, sticky=tk.W, pady=5)
        self.new_product_stock_entry = ttk.Entry(self.main_frame, width=5)
        self.new_product_stock_entry.grid(row=4, column=5, pady=5)

        self.add_product_button = ttk.Button(self.main_frame, text="Add New Product", command=self.handle_add_product)
        self.add_product_button.grid(row=5, column=4, padx=5, pady=5)

        # Ürün çıkarma
        ttk.Label(self.main_frame, text="Remove Product (Name):").grid(row=5, column=0, sticky=tk.W, pady=5)
        self.remove_product_entry = ttk.Entry(self.main_frame)
        self.remove_product_entry.grid(row=5, column=1, pady=5)
        self.remove_product_button = ttk.Button(self.main_frame, text="Remove", command=self.handle_remove_product)
        self.remove_product_button.grid(row=5, column=2, padx=5, pady=5)

        # Listbox
        self.products_text = tk.Text(self.main_frame, width=70, height=12, state=tk.DISABLED)
        self.products_text.grid(row=6, column=0, columnspan=7, pady=10)

    #Cıkış
    def logout(self):
        self.current_employee = None
        self.create_login_frame()

    #Satış fonk
    def handle_sale(self):
        product_name = self.sale_product_entry.get().strip()
        qty_text = self.sale_qty_entry.get().strip()
        product = self.inventory.get_product(product_name)
        if not product:
            messagebox.showerror("Error", "Product is not found.")
            return
        try:
            qty = int(qty_text)
            if qty <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")
            return
        if product.stock >= qty:
            product.remove_stock(qty)
            total_price = product.price * qty
            self.current_employee.transactions_increment()
            messagebox.showinfo("Sales", f"Total Price: {total_price} TL\nSales succesful.")
            self.show_inventory()
        else:
            messagebox.showerror("Error", "There is no enough stock.")

    #Stok ekleme fonk
    def handle_stock_add(self):
        product_name = self.stock_product_entry.get().strip()
        qty_text = self.stock_qty_entry.get().strip()
        product = self.inventory.get_product(product_name)
        if not product:
            messagebox.showerror("Error", "Product is not found")
            return
        try:
            qty = int(qty_text)
            if qty <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive number.")
            return
        product.add_stock(qty)
        messagebox.showinfo("Succesful", f"{qty} piece stocks added. New Stock: {product.stock}")
        self.show_inventory()

    #List box fonk
    def show_inventory(self):
        self.products_text.config(state=tk.NORMAL)
        self.products_text.delete(1.0, tk.END)
        self.products_text.insert(tk.END, "Product Name\t    Price ($)\t     Stock\n")
        self.products_text.insert(tk.END, "-"*40 + "\n")
        for p in self.inventory.products.values():
            self.products_text.insert(tk.END, f"{p.name}\t         {p.price:.2f}\t           {p.stock}\n")
        self.products_text.config(state=tk.DISABLED)

    #İşlem sayaç
    def show_transaction_count(self):
        count = self.current_employee.get_transactions()
        messagebox.showinfo("Daily Transaction Count", f"Total Transaction Count: {count}")

    #Ürün ekleme fonk
    def handle_add_product(self):
        name = self.new_product_name_entry.get().strip()
        if self.inventory.get_product(name):
            messagebox.showerror("Error", "There is already have a same product.")
            return
        price_text = self.new_product_price_entry.get().strip()
        stock_text = self.new_product_stock_entry.get().strip()
        try:
            price = float(price_text)
            stock = int(stock_text)
            if price <= 0 or stock < 0:
                messagebox.showerror("Error", "Price must be positive and stock must be zero or greater.")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid price and stock.")
            return
        new_product = Item(name, price, stock)
        self.inventory.add_product(new_product)
        messagebox.showinfo("Succesful", f"'{name}' added succesfully.")
        self.show_inventory()

    #Ürün çıkarma fonk
    def handle_remove_product(self):
        name = self.remove_product_entry.get().strip()
        product = self.inventory.get_product(name)
        if not product:
            messagebox.showerror("Error", "Product is not found.")
            return
        confirm = messagebox.askyesno("Confirmation", f"'{name}' Are you sure to remove this product?")
        if confirm:
            del self.inventory.products[name]
            messagebox.showinfo("Succesful", f"'{name}' removed.")
            self.show_inventory()

if __name__ == "__main__":
    app = CashierApp()
    app.mainloop()
