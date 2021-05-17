from flask import Flask, render_template, request
from functions import calc1, calc2

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        ci = float(request.form['ci'])
        gv = float(request.form['gv'])
        xz = float(request.form['xz'])
        xp = float(request.form['xp'])
        xr = float(request.form['xr'])
        res_1 = calc1(ci, gv, xz, xp, xr)
        res1 = list(map(lambda x: round(x, 2), res_1))
        xr2  = request.form['xr2']
        if xr2 != "":
            xr2 = float(xr2)
            res_2 = calc2(ci, gv, xz, xp, xr, xr2)
            res2 = list(map(lambda x: round(x, 2), res_2))
        else:
            res2 = ()
        return render_template('index.html', res1=res1, res2=res2, data=(ci, gv, xz, xp, xr, xr2))
    else:
        return render_template('index.html', res1=(), res2=(), data=())
 
if __name__ == "__main__":
    app.run(debug=True)