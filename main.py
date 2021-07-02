
from flask import Flask,request,render_template
app = Flask(__name__)


@app.route("/",methods=["GET","POST"])


def main():
    if request.method=="POST":
        resp = request.form


        if resp.get('opt')== 'Fluffy Ragdoll Cat':
            result = "Price is: 27K "
            return render_template("result1.html", resp=result)

        elif resp.get('opt') == 'Persian Cat':
            result = "Price is: 20K "
            return render_template("result2.html", resp=result)


        elif resp.get('opt') == 'Norwegian Forest Cat':
            result = "Price is: 35K "
            return render_template("result3.html", resp=result)



    else:

        return render_template("input.html")




if __name__ == '__main__':
    app.run(debug=True)
