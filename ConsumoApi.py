import tkinter as tk
from tkinter import messagebox
import requests

def login():
    email = email_entry.get()
    password = password_entry.get()

    url = "https://consumo-de-api-y-publicacion-taller-62-is.up.railway.app/auth/login"
    payload = {
        "email": email,
        "password": password
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 201:
        messagebox.showinfo("Se ha logueado correctamente!!!!", f"Response: {response.json()}")
    else:
        messagebox.showerror("Ingrese las Credenciales Correctas :(", f"Status Code: {response.status_code}\nResponse: {response.json()}")

# Crear la ventana principal
root = tk.Tk()
root.title("Login")

# Crear y colocar las etiquetas y entradas
tk.Label(root, text="Correo").grid(row=0, column=0, padx=10, pady=10)
email_entry = tk.Entry(root)
email_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Contraseña").grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Botón de login
login_button = tk.Button(root, text="Iniciar Sesión", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Iniciar el bucle de la aplicación
root.mainloop()
