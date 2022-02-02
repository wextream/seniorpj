from flask import Flask, render_template
import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import base64
from HMprep import HM_matrix

app = Flask(__name__,template_folder='templates')

@app.route('/')
def display_png():
    image , heatmap_matrix = HM_matrix('IMG_1258_s.jpg',gaussian_std=2)
    fig , ax = plt.subplots(figsize=(6,3.5))
    fig.subplots_adjust(0,0,1,1)
    ax.axis('off')
    ax.imshow(image)
    ax.imshow(heatmap_matrix/255, alpha=0.3, cmap='seismic')

    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)

    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

    return render_template("index2.html", image=pngImageB64String)

if __name__ == '__main__':
    app.run()



