from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

def convert():
    try:
        if Area_combo.get() == "Acres":
            #Acres to Squre feet
            if Area_combo2.get() == "Squre feet":
                Area_entry2.delete(0, END)
                str_value = Area_entry.get()
                int_value = int(str_value)
                converted_num  = int_value * 43560
                Area_entry2.insert("end", f"{converted_num}")
            #Acres to Squre centimetres
            elif Area_combo2.get() == "Squre centimetres":
                Area_entry2.delete(0, END)
                str_value = Area_entry.get()
                int_value = int(str_value)
                converted_num = int_value * 0.001076391
                Area_entry2.insert("end", f"{converted_num}")
            #Acres to Squre inches
            elif Area_combo2.get() == "Squre inches":
                Area_entry2.delete(0, END)
                str_value = Area_entry.get()
                int_value = int(str_value)
                converted_num = int_value * 0.0069444444
                Area_entry2.insert("end", f"{converted_num}") 
            #Acres to Squre metres
            elif Area_combo2.get() == "Squre metres":
                Area_entry2.delete(0, END)
                str_value = Area_entry.get()
                int_value = int(str_value)
                converted_num = int_value * 10.7639104167
                Area_entry2.insert("end", f"{converted_num}")
    except:
        Area_entry2.insert("end", "Convert Error")

#App
root = customtkinter.CTk()
root.title("Unit Converter")
root.geometry("780x500")

#Labels
title = customtkinter.CTkLabel(root, text="Unit Converter", font=("Helvatica", 20))
title.pack(pady=10)

Area_label = customtkinter.CTkLabel(root, text="Area", font=("Helvatica", 15), text_color="red")
Area_label.place(x=370, y=60)

#Combo Boxes
Area = ["Squre feet", "Squre centimetres", "Squre inches", "Squre metres"]
Area1 = ["Acres"]
Area_combo = customtkinter.CTkComboBox(root, values=Area1)
Area_combo.place(x=10, y=100)

Area_combo2 = customtkinter.CTkComboBox(root, values=Area)
Area_combo2.place(x=620, y=100)

#Entrys
Area_entry = customtkinter.CTkEntry(root)
Area_entry.place(x=160, y=100)

Area_entry2 = customtkinter.CTkEntry(root)
Area_entry2.place(x=470, y=100)

#Buttons
Area_convert = customtkinter.CTkButton(root, text="Convert", command=convert)
Area_convert.place(x=315, y=100)


#Run the App
root.mainloop()