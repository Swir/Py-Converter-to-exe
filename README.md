<div align="center">

# 📦 Py Converter To EXE / APP

**Graphical Python packaging helper by Swir**  
**Graficzny pomocnik do pakowania programów Python autorstwa Swir**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![PyInstaller](https://img.shields.io/badge/Windows-PyInstaller-0078D4)
![py2app](https://img.shields.io/badge/macOS-py2app-111111?logo=apple)
![Author](https://img.shields.io/badge/Author-Swir-ff4fa3)

</div>

---

## 🇬🇧 English

Py Converter To EXE is a Tkinter desktop front-end that simplifies packaging Python scripts into standalone applications. The interface lets you select a `.py` file, choose the target type and watch packaging output in an integrated terminal area.

### ✨ Features
- graphical `.py` file selection
- Windows `.exe` target
- macOS `.app` target
- console / no-console option
- packaging performed in a background thread
- integrated build-output panel
- platform-aware packaging workflow

### 🚀 Installation

```bash
git clone https://github.com/Swir/Py-Converter-to-exe.git
cd Py-Converter-to-exe
pip install -r requirements.txt
python converterpy.py
```

> Windows builds use PyInstaller; macOS application bundles require a compatible macOS environment and py2app.

---

## 🇵🇱 Polski

Py Converter To EXE to graficzna nakładka Tkinter ułatwiająca pakowanie skryptów Python do samodzielnych aplikacji. Wybierasz plik `.py`, typ wynikowy i obserwujesz przebieg procesu w zintegrowanym polu terminala.

### ✨ Funkcje
- graficzny wybór pliku `.py`
- generowanie `.exe` dla Windows
- generowanie `.app` dla macOS
- opcja z konsolą / bez konsoli
- pakowanie w osobnym wątku
- podgląd komunikatów procesu
- obsługa zależna od systemu operacyjnego

### 🚀 Instalacja

```bash
pip install -r requirements.txt
python converterpy.py
```

> Pakiety należy budować na odpowiednim systemie docelowym; aplikacja nie zastępuje wymagań PyInstaller/py2app.

## 👤 Author / Autor
Developed by **Swir**.
