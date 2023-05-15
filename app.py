from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template("paginas/index.html", \
        titulo_pagina="Página inicial")

@app.route("/esporte")
def categorias():
    return render_template("paginas/esporte.html", \
        titulo_pagina="Esporte")

@app.route("/economia")
def produto():
    return render_template("paginas/economia.html", \
        titulo_pagina="Economia")
    
@app.route("/educacao")
def carrinho():
    return render_template("paginas/educacao.html", \
        titulo_pagina="Educacao")

@app.route("/tecnologia")
def pagamento():
    return render_template("paginas/tecnologia.html", \
        titulo_pagina="Tecnologia")
    
if __name__ == "__main__":
    app.run(debug=True)