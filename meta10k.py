import json
import os
from datetime import date
import tkinter as tk
from tkinter import messagebox

ARQUIVO_PROGRESO = "progresso.json"
dias = list(range(1, 142))
valores = [i for i in dias]

def carregar_progresso():
    if os.path.exists(ARQUIVO_PROGRESO):
        with open(ARQUIVO_PROGRESO, "r") as f:
            return json.load(f)
    return {"dias_completos": []}

def salvar_progresso(progresso):
    with open(ARQUIVO_PROGRESO, "w") as f:
        json.dump(progresso, f)

def mostrar_status():
    progresso = carregar_progresso()
    dias_completos = progresso["dias_completos"]
    total = sum(valores[dia - 1] for dia in dias_completos)
    
    status_text = f"📅 Dias completados: {len(dias_completos)} de 141\n"
    status_text += f"💰 Total acumulado: R$ {total:.2f}\n"

    if len(dias_completos) < 141:
        proximo_dia = len(dias_completos) + 1
        status_text += f"➡️ Próximo valor a poupar (Dia {proximo_dia}): R$ {valores[proximo_dia - 1]:.2f}"
    else:
        status_text += "🎉 Parabéns! Meta atingida."

    status_label.config(text=status_text)

def marcar_dia():
    progresso = carregar_progresso()
    proximo_dia = len(progresso["dias_completos"]) + 1
    if proximo_dia <= 141:
        progresso["dias_completos"].append(proximo_dia)
        salvar_progresso(progresso)
        messagebox.showinfo("Sucesso", f"✅ Dia {proximo_dia} registrado com sucesso!")
    else:
        messagebox.showinfo("Info", "✅ Todos os dias já foram completados!")
    mostrar_status()

# Criação da interface
root = tk.Tk()
root.title("Desafio R$ 10.000 em 141 Dias")

status_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
status_label.pack(pady=10)

btn_status = tk.Button(root, text="Ver Status", command=mostrar_status)
btn_status.pack(pady=5)

btn_marcar = tk.Button(root, text="Marcar Dia como Completo", command=marcar_dia)
btn_marcar.pack(pady=5)

btn_sair = tk.Button(root, text="Sair", command=root.quit)
btn_sair.pack(pady=5)

# Mostrar status inicial
mostrar_status()

root.mainloop()
