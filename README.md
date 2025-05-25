# The-BasicSalesApp
This program manages the stock status of items in a store's inventory, maintains a price list, and generates sales invoices. It aims to simplify cashier tasks by providing an efficient, user-friendly interface to process sales, update stock.

## 📦 Features

- Developed in Python 3
- Single-file executable using PyInstaller
- Runs on 64-bit Linux systems
- No additional setup required

## 🚀 Installation (Linux)

Download and run the app with the following commands:

```
wget https://github.com/EEKGG/The-BasicSalesApp/releases/download/v1.5-for-Linux-distros/SalesApp v1.5.tar.gz
unzip SalesApp v1.5.tar.gz
chmod +x BasicSalesApp
./BasicSalesApp
```


Note: If you uploaded the binary directly (not zipped), you can skip the unzip step.

## 🛠️ Build It Yourself (Optional)

If you want to build the application yourself on your own Linux system:

1. Make sure you have Python 3 installed.

2. Install PyInstaller:
`pip install pyinstaller`

3. Clone this repository and go into the project folder:
```
git clone https://github.com/EEKGG/The-BasicSalesApp/releases/download/v1.5-for-Linux-distros/SalesApp v1.5.tar.gz
cd The-BasicSalesApp
```

5. Build the standalone executable:
`pyinstaller --onefile main.py`

> If you wanna add a logo on your app
`pyinstaller --onefile --icon=logo.ico main.py`

> Replace main.py with your actual Python file name if it's different

6. After the build completes, the executable will be located in the `dist/` folder:
```
cd dist
./main
```
You may need to make it executable first:

`chmod +x main`

✅ This will generate a self-contained binary that can run on most 64-bit Linux distributions without needing Python installed.
















## Contributors

<a href="https://github.com/ahmetzbaboo">
  <img src="https://avatars.githubusercontent.com/ahmetzbaboo?v=4" width="50px" alt="ahmetzbaboo"/>
</a>
<a href="https://github.com/ismailhadimioglu">
  <img src="https://avatars.githubusercontent.com/ismailhadimioglu?v=4" width="50px" alt="ismailhadimioglu"/>
</a>


