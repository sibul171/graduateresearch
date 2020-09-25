import responder
import io
import matplotlib.pyplot as plt
import numpy as np

api = responder.API()

# create the plot
def createPlotAndSvg():
    #棒グラフを作成する。
    x = np.arange(3)
    y = np.array([100, 30, 70])
    plt.bar(x, y)

    #plotをSVGに変換する。
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight')
    # plotをクリア
    plt.cla()   
    svg = buf.getvalue()
    buf.close()
    return svg

@api.route("/")
async def bargraph(req, resp):
    svg = createPlotAndSvg()
    resp.headers['content_type'] = 'image/svg+xml'
    resp.content = svg

api.run()