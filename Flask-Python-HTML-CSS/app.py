import base64
import numpy as np
import matplotlib.pyplot as plt

from io import BytesIO
from flask import Flask, render_template, request
from matplotlib.figure import Figure

app = Flask(__name__)
V = {}

def f(x):
    return x**6 + x**5 + x**4 + x**3 + x**2 + x

def df(x):
    return 6*x**5 + 5*x**4 + 4*x**3 + 3*x**2 + 2*x + 1

@app.route("/")
def index():
    types = ['Mandelbrot-type set', 'Newton Basins']
    return render_template("index.html", types=types)

@app.route("/draw", methods=["POST"])
def draw():
    types = ['Mandelbrot-type set', 'Newton Basins']
    try:
        global V

        # Get all values from form
        pmin = float(request.form.get("pmin"))
        pmax = float(request.form.get("pmax"))
        qmin = float(request.form.get("qmin"))
        qmax = float(request.form.get("qmax"))
        ppoints = int(request.form.get("ppoints"))
        qpoints = int(request.form.get("qpoints"))
        max_iterations = int(request.form.get("max_iterations"))
        infinity_border = int(request.form.get("infinity_border"))
        frac = request.form.get('flactal')

        # Store parameters
        V.update({
            'pmin': pmin, 'pmax': pmax, 'qmin': qmin, 'qmax': qmax,
            'ppoints': ppoints, 'qpoints': qpoints,
            'max_iterations': max_iterations, 'infinity_border': infinity_border
        })

        # Generate image
        image = np.zeros((ppoints, qpoints))
        if frac == 'Newton Basins':
            p, q = np.mgrid[pmin:pmax:(ppoints*1j), qmin:qmax:(qpoints*1j)]
            c = p + 1j*q
            z = np.zeros_like(c)
            for k in range(max_iterations):
                z = z - f(c) / df(c)
                mask = (np.abs(z) > infinity_border) & (image == 0)
                image[mask] = k
                z[mask] = np.nan
        else:
            for ip, p in enumerate(np.linspace(pmin, pmax, ppoints)):
                for iq, q in enumerate(np.linspace(qmin, qmax, qpoints)):
                    c = p + 1j * q
                    z = 0
                    for k in range(max_iterations):
                        z = z**2 + c
                        if abs(z) > infinity_border:
                            image[ip, iq] = k
                            break

        # Generate figure
        fig = Figure()
        ax = fig.subplots()
        ax.set_xticks([])
        ax.set_yticks([])
        ax.imshow(-image.T, cmap='flag')
        buf = BytesIO()
        fig.savefig(buf, format="png")
        data = base64.b64encode(buf.getbuffer()).decode("ascii")

        return render_template("index.html", data=data, types=types, summary=V, selected=frac)

    except Exception as e:
        return render_template("index.html", error='⚠️ Invalid input. Please try again.', types=types)

if __name__ == "__main__":
    app.run(debug=True)