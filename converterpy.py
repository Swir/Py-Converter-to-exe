import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from ttkthemes import ThemedTk
import subprocess
import threading
import platform

class PyToExeConverter:
    def __init__(self, master):
        self.master = master
        master.title("PyToExe Converter")

        self.label = ttk.Label(master, text="Wybierz plik .py:")
        self.label.grid(row=0, column=0, pady=10, sticky="w", padx=10)

        self.select_button = ttk.Button(master, text="Wybierz plik", command=self.select_file)
        self.select_button.grid(row=0, column=1, pady=10, padx=10)

        self.execution_type = tk.StringVar()
        self.execution_type.set("exe")

        self.exe_button = ttk.Radiobutton(master, text=".exe", variable=self.execution_type, value="exe")
        self.exe_button.grid(row=0, column=2, pady=10, padx=10)

        self.app_button = ttk.Radiobutton(master, text=".app", variable=self.execution_type, value="app")
        self.app_button.grid(row=0, column=3, pady=10, padx=10)

        self.convert_button = ttk.Button(master, text="Konwertuj", command=self.convert_to_exe)
        self.convert_button.grid(row=1, column=0, columnspan=4, pady=10, padx=10)

        self.terminal = tk.Text(master, height=10, width=60)
        self.terminal.grid(row=2, column=0, columnspan=4, pady=10, padx=10)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Pliki Python", "*.py")])
        self.file_path = file_path
        self.label.config(text=f"Wybrano plik: {file_path}")

    def convert_to_exe(self):
        if hasattr(self, 'file_path') and self.file_path:
            # Resetuj terminal
            self.terminal.delete("1.0", tk.END)

            # Uruchom konwersję w osobnym wątku
            threading.Thread(target=self.run_conversion).start()
        else:
            self.update_terminal("Wybierz plik .py przed konwersją.")

    def run_conversion(self):
        try:
            # Sprawdź, czy system operacyjny to macOS
            is_macos = platform.system() == 'Darwin'

            # Uruchom pyinstaller w procesie
            with subprocess.Popen(
                ['pyinstaller', '--onefile', self.file_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                universal_newlines=True,
            ) as process:

                # Przekieruj standardowe wyjście i błąd do funkcji obsługi
                for line in process.stdout:
                    self.update_terminal(line.strip())

                # Sprawdź, czy proces zakończył się
                process.wait()

                if process.returncode == 0:
                    if is_macos and self.execution_type.get() == "app":
                        self.update_terminal("Konwersja do .app zakończona pomyślnie.")
                    elif not is_macos and self.execution_type.get() == "app":
                        self.update_terminal("Konwersja do .app jest obsługiwana tylko na systemie macOS.")
                    else:
                        self.update_terminal("Konwersja zakończona pomyślnie.")
                else:
                    self.update_terminal(f"Błąd podczas konwersji. Kod powrotu: {process.returncode}")

        except Exception as e:
            self.update_terminal(f"Błąd podczas uruchamiania procesu: {str(e)}")

    def update_terminal(self, message):
        self.terminal.insert(tk.END, message + "\n")
        self.terminal.see(tk.END)

if __name__ == "__main__":
    root = ThemedTk(theme="ubuntu")
    app = PyToExeConverter(root)
    root.mainloop()
