<!-- SWIR-README-STANDARD:v2 -->

<div align="center">

<img width="100%" src="assets/readme/hero.svg" alt="Py Converter to EXE — Tkinter frontend for packaging Python scripts with PyInstaller" />

<br>

![Python](https://img.shields.io/badge/Python-3.x-02050A?style=for-the-badge&logo=python&logoColor=62E5FF)
![Windows](https://img.shields.io/badge/Windows-PyInstaller-02050A?style=for-the-badge&logo=windows11&logoColor=62E5FF)
![GUI](https://img.shields.io/badge/GUI-Tkinter-02050A?style=for-the-badge&logo=python&logoColor=62E5FF)
![Release](https://img.shields.io/badge/Release-v1.0.0-02050A?style=for-the-badge&logo=github&logoColor=62E5FF)

[![Author](https://img.shields.io/badge/Author-Swir-0088FF?style=flat-square&logo=github)](https://github.com/Swir)

</div>

# Py Converter to EXE

A small Tkinter desktop frontend for selecting a Python script and running PyInstaller with one-file packaging while streaming the build output inside the application.

## 📍 Project Status

<p align="center">
  <img width="100%" src="assets/readme/progress-card.svg" alt="Py Converter to EXE product progress — N/A because the repository has no authoritative product roadmap" />
</p>

| Item | Status |
|---|---|
| Current stage | Maintained legacy utility |
| Primary packaging engine | PyInstaller |
| Latest public release | [v1.0.0](https://github.com/Swir/Py-Converter-to-exe/releases/tag/v1.0.0) |
| Product progress | **N/A** — no authoritative measurable roadmap exists |

## 🚀 Overview

The current implementation lets you choose a `.py` file, select whether the generated program should keep a console window, and start a PyInstaller `--onefile` build on a worker thread. Build output is shown in the GUI so the interface remains responsive during packaging.

The interface includes `.exe` and `.app` radio buttons, but the current source always invokes **PyInstaller**. The `.app` option does **not** invoke `py2app`; on non-macOS hosts it only reports that `.app` is macOS-only after the PyInstaller process completes. For that reason this README does not advertise a verified py2app workflow.

## ✨ Highlights

| Feature | What it does |
|---|---|
| 📂 Python file picker | Selects the input `.py` script with a native Tkinter dialog |
| 📦 One-file packaging | Runs `pyinstaller --onefile` for the selected script |
| 🖥️ Console toggle | Adds `--noconsole` when the console option is disabled |
| 🧵 Background build | Runs packaging work in a separate thread |
| 📟 Integrated log | Streams PyInstaller stdout/stderr into the application window |
| 🎨 Themed Tk UI | Uses `ttkthemes` with the `arc` theme |

## ⚙️ Quick Start

### Recommended release package

The current public release is **v1.0.0**. It contains a source ZIP plus a matching SHA-256 file; it is **not** a prebuilt Windows EXE.

[**Open v1.0.0 →**](https://github.com/Swir/Py-Converter-to-exe/releases/tag/v1.0.0)

### From source

```bash
git clone https://github.com/Swir/Py-Converter-to-exe.git
cd Py-Converter-to-exe
python -m pip install ttkthemes pyinstaller
python converterpy.py
```

> `requirements.txt` is a legacy command-style file containing `pip install ...`, so it is not a conventional requirements file for `pip install -r requirements.txt`.

## 📋 Requirements / Compatibility

- Python 3.x with Tkinter available.
- `ttkthemes` for the themed GUI.
- PyInstaller available on `PATH` as the `pyinstaller` command.
- Build on the target operating system when you need native platform output; this utility does not provide a verified cross-compilation layer.
- macOS `.app` creation is **not** implemented as a separate py2app pipeline in the current source.

## 🎮 Usage

1. Start `converterpy.py`.
2. Choose the Python source file.
3. Select the desired interface option and whether the generated program should keep a console.
4. Click **Konwertuj**.
5. Follow PyInstaller output in the integrated terminal panel.

PyInstaller normally writes its generated build files according to its own defaults, including a `dist` directory unless overridden externally.

## 🧠 Technology

| Layer | Technology / role |
|---|---|
| GUI | Tkinter / ttk + ttkthemes |
| Packaging | PyInstaller command-line process |
| Background work | Python `threading.Thread` |
| Process output | `subprocess.Popen` with merged stdout/stderr |

## 🗺️ Roadmap / Progress

<p align="center">
  <img width="100%" src="assets/readme/progress-mini.svg" alt="Py Converter to EXE product progress — N/A" />
</p>

**Product completion: N/A.** This repository does not currently contain a trustworthy product roadmap or measurable completion denominator, so no application-readiness percentage is invented.

The SVG files are generated deterministically by `tools/generate_progress.py` and can be checked with:

```bash
python tools/generate_progress.py --check
```

## 📦 Releases

Latest verified public release: **v1.0.0**.

- `Py-Converter-to-exe-v1.0.0.zip`
- `Py-Converter-to-exe-v1.0.0.zip.sha256`

[**GitHub Releases →**](https://github.com/Swir/Py-Converter-to-exe/releases)

## ⚠️ Limitations

- The current source does not implement py2app despite the historical `.app` UI label.
- Packaging success depends on PyInstaller compatibility with the selected script and its dependencies.
- The GUI does not provide advanced PyInstaller configuration such as icons, hidden imports, data-file mapping or custom spec editing.
- The repository does not contain an authoritative product roadmap, so product progress remains N/A.

## 🔎 Search Keywords

`python to exe converter` • `pyinstaller gui` • `python executable builder` • `tkinter pyinstaller frontend` • `python desktop packaging` • `pyinstaller onefile gui` • `windows python exe builder` • `python script packager` • `ttkthemes tkinter app` • `python build log gui` • `pyinstaller noconsole` • `python packaging utility`

<div align="center">

### `BUILD • PACKAGE • VERIFY • EVOLVE`

⭐ **If this project is useful, consider leaving a star.**

[**← SWIR profile**](https://github.com/Swir) · [**All projects →**](https://github.com/Swir?tab=repositories)

</div>
