import tkinter as tk

def decimal_to_binary():
    try:
        decimal_num = int(input_field.get())
        binary_num = bin(decimal_num).replace("0b", "")
        output_label.config(text=f"Binary: {binary_num}")
    except ValueError:
        output_label.config(text="Invalid input. Please enter a decimal number.")

def binary_to_decimal():
    try:
        binary_num = input_field.get()
        decimal_num = int(binary_num, 2)
        output_label.config(text=f"Decimal: {decimal_num}")
    except ValueError:
        output_label.config(text="Invalid input. Please enter a valid binary number.")

def clear_output():
    output_label.config(text="")
    input_field.delete(0, tk.END)

root = tk.Tk()
root.title("Binary-Decimal Converter")

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

decimal_to_binary_button = tk.Button(button_frame, text="Decimal to Binary", command=decimal_to_binary)
decimal_to_binary_button.pack(side=tk.LEFT, padx=5)

binary_to_decimal_button = tk.Button(button_frame, text="Binary to Decimal", command=binary_to_decimal)
binary_to_decimal_button.pack(side=tk.LEFT, padx=5)

# Entry field
input_label = tk.Label(root, text="Enter Number:")
input_label.pack()

input_field = tk.Entry(root)
input_field.pack(pady=5)

# Convert and Clear buttons
convert_button = tk.Button(root, text="Convert", command=lambda: None)  # Placeholder for now
convert_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear", command=clear_output)
clear_button.pack(pady=5)

# Output label
output_label = tk.Label(root, text="", pady=10)
output_label.pack()

root.mainloop()
