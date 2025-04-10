# 🌌 Fractal Visualizer

An interactive web-based fractal visualizer built with **Python (Flask + Matplotlib)**.  
Allows users to explore complex mathematical structures like **Mandelbrot-like sets** and **Newton basins** by customizing input ranges and parameters.

![screenshot](static/demo.png)

---

## ✨ Features

- 🌀 Choose between Mandelbrot-type or Newton fractals
- 🎛️ Custom input: axis ranges, resolution, iteration depth
- 📷 Live fractal rendering in browser
- 💻 Simple & clean Flask-powered frontend (HTML/CSS)
- ⚡ Fast rendering using NumPy & Matplotlib

---

## 🛠 Technologies Used

- Python 3
- Flask
- NumPy
- Matplotlib
- HTML/CSS (Jinja templating)

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/JustRusslan/fractal-visualizer.git
cd fractal-visualizer/Flask-Python-HTML-CSS
pip install -r ../requirements.txt
flask --app app run
