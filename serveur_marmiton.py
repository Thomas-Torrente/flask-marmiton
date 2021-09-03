from flask import Flask, request, redirect, render_template

from data_marmitton import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", result=allAfficher())


@app.route("/recette/<title>")
def detailRecette(title):
    return render_template("detail_recette.html", resultOneRecette=oneAfficher(title))


@app.route("/ajouter", methods=["POST", "GET"])
def ajouter():
    if request.method == "POST":
        newRecette = ajouterRecette(request.form["title"], request.form["ingredients"], request.form["content"],
                                    request.form["time"], request.form["image"], request.form["type"], request.form["difficulty"], request.form["persons"])
        return render_template("index.html", result=allAfficher())
    else:
        return render_template("add.html")


@app.route("/rechercher", methods=["POST", "GET"])
def search():
    if request.method == "POST":
        searchRecette = rechercherRecette(request.form["ingredients"])
        return render_template("search.html", searchRecette=searchRecette)
    else:
        return render_template("search.html")


# rechercher par type (ex : apero, dessert etc...)

@app.route("/pastis-par-temps-bleu/pastis-delicieux")
def apperoAfficher():
    return render_template("apero.html", resultApero=apero())


@app.route("/entree")
def entreeAfficher():
    return render_template("entree.html", resultEntree=entree())


@app.route("/plat")
def platAfficher():
    return render_template("plat.html", resultPlat=plat())


@app.route("/dessert")
def dessertAfficher():
    return render_template("dessert.html", resultDessert=desserts())


@app.route("/delete", methods=["POST", "GET"])
def supp():
    if request.method == "POST":
        delRecette = delete(request.form["title"])
        return render_template("index.html", delRecette=delRecette, listAffiche=allAfficher())
    else:
        return render_template("delete.html")


if __name__ == "__main__":
    app.run(debug=True)
