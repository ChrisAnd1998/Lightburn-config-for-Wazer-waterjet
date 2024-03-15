import serial
import os
import serial.tools.list_ports
from tkinter import filedialog, messagebox
import tkinter as tk

class SerialUploader:
    def __init__(self, port, baudrate):
        self.serial_port = serial.Serial(port, baudrate)
        self.serial_port.timeout = 2  # Timeout for readline method

    def upload_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                file_content = file.read()
                upload_command = f"upload {os.path.basename(file_path)}\n{file_content}\n\x04"
                if self.serial_port.is_open:
                    self.serial_port.write(upload_command.encode())
        except Exception as e:
            messagebox.showerror("Error", f"Failed to connect to Smoothieboard: {e}")
            if self.serial_port.is_open:
                self.serial_port.close()

    def check_response(self):
        while self.serial_port.is_open:
            received_data = self.serial_port.readline().decode().strip()
            if received_data.startswith("uploaded"):
                self.serial_port.write(b"M21\n")
                self.serial_port.write(b"G0 Y-1\n")
                self.serial_port.write(b"G0 Y1\n")
                self.serial_port.write(b"G0 Y-1\n")
                self.serial_port.write(b"G0 Y1\n")
                messagebox.showinfo("Upload Complete", f"Successfully {received_data}!")
                self.serial_port.close()
                break

def find_smoothie_port():
    smoothie_port = None
    ports = serial.tools.list_ports.comports()
    for port_info in ports:
        port = port_info.device
        try:
            serial_port = serial.Serial(port)
            serial_port.timeout = 2
            serial_port.write(b"version\n")
            response = serial_port.readline().decode().strip()
            print(f"Port: {port}, Response: {response}")  # Print the port and its response
            if "Build version:" in response:
                smoothie_port = port
                serial_port.write(b"G0 Y-1\n")
                serial_port.write(b"G0 Y1\n")
                break
            serial_port.close()
        except Exception as e:
            pass  # Ignore ports that cannot be accessed
    return smoothie_port


def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(filetypes=[("G-code files", "*.gc *.gcode")])
    return file_path

if __name__ == "__main__":
    smoothie_port = find_smoothie_port()
    if smoothie_port:
        messagebox.showinfo("Smoothieboard Found", f"Found Smoothieboard on port: {smoothie_port}")
        uploader = SerialUploader(smoothie_port, 115200)
        file_path = select_file()
        if file_path:
            uploader.upload_file(file_path)
            uploader.check_response()
        else:
            messagebox.showerror("Error", "No file selected.")
    else:
        messagebox.showerror("Error", "Smoothieboard not found on any available port.")
