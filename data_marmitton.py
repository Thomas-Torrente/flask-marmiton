import os
import sqlite3

os.chdir("C:/Users/thoma/OneDrive/Bureau/Python/BlaBlacode/Flask/marmiton/2.0")

DATA_URL = "data/marmitonDB.sqlite"
# la ou se trouve la BDD

conn = sqlite3.connect(DATA_URL)
# connexion a la BDD
conn.row_factory = sqlite3.Row

cursor = conn.cursor()

# try:
#     sql = """ CREATE TABLE IF NOT EXISTS recipe ( title text, ingredients text, content text, comment text, time text, type text, difficulty text, persons number  ) """
#     # Si la table "recipe" n'existe pas alors la créer
#     cursor.execute(sql)

#     conn.commit()

# finally:
#     print('table check ends')
#     conn.close()


def allAfficher():
    """Permets d'afficher le titre et l'image d'une recette title text, image text, """

    R = []
    conn = sqlite3.connect(DATA_URL)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * from recipe")
    # on selectionne tous ce qu'il y a dans recipe

    for i in cursor:
        ma_recette = {}
        # on fais un dictionnary
        ma_recette["title"] = i["title"]
        ma_recette["image"] = i["image"]
        # et on stoque dedans a chaque tour de boucle le titre et l'image de chaque ligne
        R.append(ma_recette)
    return R
    # OUBLIE PAS LE RETURNNN !!!!


def oneAfficher(title):
    """Permets d'afficher tous les élèments contenues des recettes : title text, ingredients text, content text, comment text, time text, image text, persons number, type text, difficulty text"""
    O = []
    conn = sqlite3.connect(DATA_URL)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * from recipe where title == ? ", (title,))

    for i in cursor:
        une_recette = {}
        une_recette["title"] = i["title"]
        une_recette["ingredients"] = i["ingredients"]
        une_recette["content"] = i["content"]
        une_recette["comment"] = i["comment"]
        une_recette["time"] = i["time"]
        une_recette["image"] = i["image"]
        une_recette["persons"] = i["persons"]
        une_recette["type"] = i["type"]
        une_recette["difficulty"] = i["difficulty"]
        O.append(une_recette)

    return O
    # OUBLIE PAS LE RETURNNN !!!!


def ajouterRecette(title, ingredients, content, time, image, type, difficulty, persons):
    # en passe en parametre tout ce qu'il faut pour créer une recette
    conn = sqlite3.connect(DATA_URL)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    chemin = "../static/images/" + image
    # on fait une variable on on stoque le chemin d'acces de l'image et l'image

    try:
        cursor.execute("INSERT INTO recipe VALUES ( ? ,  ? , ? , ? , ? , ? , ? , ? , ? , ? )",
                       (title, ingredients, content, "Incroyable", time, chemin, 0, type, difficulty, persons,))
        #    on insert les values vides pour l'instant sauf pour le commentaire qui est "incroyable"
        conn.commit()

    finally:
        return "Recette ajouté ajoutée"

    # OUBLIE PAS LE RETURNNN !!!!


def rechercherRecette(ingredients):
    # on met en parametre ingredients
    I = []
    conn = sqlite3.connect(DATA_URL)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    regexp = "%" + ingredients + "%"
    #  on créer la variable regexp et contiens ???? et ingredients

    cursor.execute("SELECT * from recipe WHERE ingredients like ?", (regexp,))

    for b in cursor:
        recetteChercher = {}
        recetteChercher["ingredients"] = b["ingredients"]
        recetteChercher["title"] = b["title"]
        recetteChercher["image"] = b["image"]
        I.append(recetteChercher)
    return I
    # OUBLIE PAS LE RETURNNN !!!!


def apero():
    A = []
    conn = sqlite3.connect(DATA_URL)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    type = "apéritif"
    cursor.execute("SELECT * from recipe WHERE type == ?", (type,))

    for i in cursor:
        recetteApero = {}
        recetteApero["type"] = i["type"]
        recetteApero["title"] = i["title"]
        recetteApero["image"] = i["image"]
        A.append(recetteApero)
    return A

    # OUBLIE PAS LE RETURNNN !!!!


def entree():
    E = []
    conn = sqlite3.connect(DATA_URL)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    type = "entrée"
    cursor.execute("SELECT * from recipe WHERE type == ?", (type,))

    for i in cursor:
        recetteEntree = {}
        recetteEntree["type"] = i["type"]
        recetteEntree["title"] = i["title"]
        recetteEntree["image"] = i["image"]
        E.append(recetteEntree)
    return E


def plat():
    P = []
    conn = sqlite3.connect(DATA_URL)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    type = "plat"
    cursor.execute("SELECT * from recipe WHERE type == ?", (type,))

    for i in cursor:
        recettePlat = {}
        recettePlat["type"] = i["type"]
        recettePlat["title"] = i["title"]
        recettePlat["image"] = i["image"]
        P.append(recettePlat)
    return P


def desserts():
    D = []
    conn = sqlite3.connect(DATA_URL)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    type = "dessert"
    cursor.execute("SELECT * from recipe WHERE type == ?", (type,))

    for i in cursor:
        recetteDesserts = {}
        recetteDesserts["type"] = i["type"]
        recetteDesserts["title"] = i["title"]
        recetteDesserts["image"] = i["image"]
        D.append(recetteDesserts)
    return D


def delete(title):
    conn = sqlite3.connect(DATA_URL)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM recipe WHERE title == ?", (title,))
        conn.commit()

    finally:
        return "Fiche supprimé avec succes"
