
from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Activități distribuite pe zilele săptămânii conform obiectivelor lui Alec
activitati_saptamana = {
    "Luni": [
        "Trezire la 5:45",
        "Stretching dimineața",
        "Apă cu semințe de chia",
        "Luarea vitaminelor",
        "10.000 pași",
        "Antrenament la sală",
        "Timp cu fetele",
        "Gest frumos pentru soție",
        "Citit 15-30 min",
        "Muncă 4-5h",
        "Curățenie (30-60 min)"
    ],
    "Marți": [
        "Trezire la 5:45",
        "Stretching dimineața",
        "Apă cu semințe de chia",
        "Luarea vitaminelor",
        "10.000 pași",
        "Timp cu fetele",
        "Gest frumos pentru soție",
        "Citit 15-30 min",
        "Muncă 4-5h",
        "Gătit meniu complet"
    ],
    "Miercuri": [
        "Trezire la 5:45",
        "Stretching dimineața",
        "Apă cu semințe de chia",
        "Luarea vitaminelor",
        "10.000 pași",
        "Antrenament la sală",
        "Timp cu fetele",
        "Gest frumos pentru soție",
        "Citit 15-30 min",
        "Muncă 4-5h",
        "Business development"
    ],
    "Joi": [
        "Trezire la 5:45",
        "Stretching dimineața",
        "Apă cu semințe de chia",
        "Luarea vitaminelor",
        "10.000 pași",
        "Timp cu fetele",
        "Gest frumos pentru soție",
        "Citit 15-30 min",
        "Muncă 4-5h",
        "Curățenie (30-60 min)"
    ],
    "Vineri": [
        "Trezire la 5:45",
        "Stretching dimineața",
        "Apă cu semințe de chia",
        "Luarea vitaminelor",
        "10.000 pași",
        "Antrenament la sală",
        "Timp cu fetele",
        "Gest frumos pentru soție",
        "Citit 15-30 min",
        "Muncă 4-5h",
        "Business development"
    ],
    "Sâmbătă": [
        "Trezire la 5:45",
        "Stretching dimineața",
        "Apă cu semințe de chia",
        "Luarea vitaminelor",
        "10.000 pași",
        "Timp cu fetele",
        "Gest frumos pentru soție",
        "Citit 15-30 min",
        "Timp cu prietenii",
        "Gătit meniu complet",
        "Curățenie (30-60 min)"
    ],
    "Duminică": [
        "Trezire la 5:45",
        "Stretching dimineața",
        "Apă cu semințe de chia",
        "Luarea vitaminelor",
        "10.000 pași",
        "Timp cu fetele",
        "Gest frumos pentru soție",
        "Citit 15-30 min",
        "Activitate recreativă (motocicletă/liniște)",
        "Organizare spațiu personal (lunar)"
    ]
}

# Stocare progres în memorie
progres = {zi: {activitate: False for activitate in activitati} for zi, activitati in activitati_saptamana.items()}

@app.route("/", methods=["GET", "POST"])
def index():
    zi_selectata = request.args.get("zi", "Luni")
    if request.method == "POST":
        for activitate in activitati_saptamana[zi_selectata]:
            progres[zi_selectata][activitate] = (activitate in request.form)
        return redirect(url_for("index", zi=zi_selectata))

    activitati = activitati_saptamana[zi_selectata]
    statusuri = progres[zi_selectata]
    zile = list(activitati_saptamana.keys())

    return render_template_string("""
    <html>
    <head>
        <title>Sistemul lui Alec - v2</title>
        <style>
            body { font-family: Arial; margin: 40px; background-color: #f4f4f4; }
            h1 { color: #333; }
            .container { background: white; padding: 20px; border-radius: 8px; max-width: 600px; margin: auto; }
            .zi-select { margin-bottom: 20px; }
            .activitate { margin: 5px 0; }
            input[type=submit] { margin-top: 20px; padding: 10px 20px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Sistemul lui Alec - Ziua: {{ zi_selectata }}</h1>
            <form method="post">
                <div class="zi-select">
                    <label for="zi">Alege ziua:</label>
                    <select id="zi" name="zi" onchange="location = '/?zi=' + this.value;">
                        {% for zi in zile %}
                            <option value="{{ zi }}" {% if zi == zi_selectata %}selected{% endif %}>{{ zi }}</option>
                        {% endfor %}
                    </select>
                </div>
                {% for activitate in activitati %}
                    <div class="activitate">
                        <input type="checkbox" name="{{ activitate }}" {% if statusuri[activitate] %}checked{% endif %}>
                        <label>{{ activitate }}</label>
                    </div>
                {% endfor %}
                <input type="submit" value="Salvează progresul">
            </form>
        </div>
    </body>
    </html>
    """, zi_selectata=zi_selectata, activitati=activitati, statusuri=statusuri, zile=zile)

if __name__ == "__main__":
    app.run(debug=True)
