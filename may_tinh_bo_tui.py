import tkinter as tk

phep_tinh = ""

def bam_nut(ky_tu):
    global phep_tinh

    if ky_tu == "=":
        try:
            ket_qua = eval(phep_tinh)
            hien_thi.set(str(ket_qua))
            phep_tinh = str(ket_qua)
        except:
            hien_thi.set("Loi")
            phep_tinh = ""

    elif ky_tu == "C":
        phep_tinh = ""
        hien_thi.set("")

    else:
        phep_tinh += ky_tu
        hien_thi.set(phep_tinh)


cua_so = tk.Tk()
cua_so.title("May tinh bo tui")
cua_so.geometry("350x450")
cua_so.resizable(False, False)

hien_thi = tk.StringVar()

o_nhap = tk.Entry(
    cua_so,
    textvariable=hien_thi,
    font=("Arial", 20),
    justify="right"
)
o_nhap.grid(row=0, column=0, columnspan=4,
            padx=10, pady=10, ipady=10)

cac_nut = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

for i, nut in enumerate(cac_nut):
    hang = i // 4 + 1
    cot = i % 4

    tk.Button(
        cua_so,
        text=nut,
        font=("Arial", 16),
        width=5,
        height=2,
        command=lambda n=nut: bam_nut(n)
    ).grid(row=hang, column=cot, padx=3, pady=3)

cua_so.mainloop()