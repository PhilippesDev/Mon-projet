""" from flask import Flask, send_from_directory

app = Flask(__name__)

# Route pour servir les fichiers statiques du dossier assets/css
@app.route('/assets/css/<path:path>')
def serve_css(path):
    return send_from_directory('iPortfolio/assets/css', path)

# Route pour servir les fichiers statiques du dossier assets/img
@app.route('/assets/img/<path:path>')
def serve_img(path):
    return send_from_directory('iPortfolio/assets/img', path)

# Route pour servir les fichiers statiques du dossier assets/js
@app.route('/assets/js/<path:path>')
def serve_js(path):
    return send_from_directory('iPortfolio/assets/js', path)

# Route pour servir les fichiers statiques du dossier assets/vendor
@app.route('/assets/vendor/<path:path>')
def serve_vendor(path):
    return send_from_directory('iPortfolio/assets/vendor', path)

# Route pour servir le fichier index.html
@app.route('/')
def index():
    return app.send_static_file('iPortfolio/index.html')

if __name__ == '__main__':
    app.run(debug=True)
 """
from flask import Flask, send_from_directory, request
import subprocess

app = Flask(__name__)

# Route pour servir les fichiers statiques du dossier assets/css
@app.route('/assets/css/<path:path>')
def serve_css(path):
    return send_from_directory('iPortfolio/assets/css', path)

# Route pour servir les fichiers statiques du dossier assets/img
@app.route('/assets/img/<path:path>')
def serve_img(path):
    return send_from_directory('iPortfolio/assets/img', path)

# Route pour servir les fichiers statiques du dossier assets/js
@app.route('/assets/js/<path:path>')
def serve_js(path):
    return send_from_directory('iPortfolio/assets/js', path)

# Route pour servir les fichiers statiques du dossier assets/vendor
@app.route('/assets/vendor/<path:path>')
def serve_vendor(path):
    return send_from_directory('iPortfolio/assets/vendor', path)

# Route pour servir le fichier index.html
@app.route('/')
def index():
    return send_from_directory('iPortfolio', 'index.html')

# Routes pour servir les autres fichiers HTML
@app.route('/Anniv.html')
def anniv():
    return send_from_directory('iPortfolio', 'Anniv.html')

@app.route('/Auto.html')
def auto():
    return send_from_directory('iPortfolio', 'Auto.html')

@app.route('/design.html')
def design():
    return send_from_directory('iPortfolio', 'design.html')

@app.route('/Designs.html')
def designs():
    return send_from_directory('iPortfolio', 'Designs.html')

@app.route('/AutresServices.html')
def autres():
    return send_from_directory('iPortfolio', 'AutresServices.html')
@app.route('/calendrier.html')
def calendari():
    return send_from_directory('iPortfolio', 'calendrier.html')
@app.route('/food.html')
def food():
    return send_from_directory('iPortfolio', 'food.html')
@app.route('/FormationDetail.html')
def formation():
    return send_from_directory('iPortfolio', 'FormationDetail.html')
@app.route('/install.html')
def install():
    return send_from_directory('iPortfolio', 'install.html')

@app.route('/maintenance.html')
def maintenance():
    return send_from_directory('iPortfolio', 'maintenance.html')

@app.route('/nosta.html')
def nosta():
    return send_from_directory('iPortfolio', 'nosta.html')

@app.route('/portfolioAtejdetails.html')
def atejd():
    return send_from_directory('iPortfolio', 'portfolioAtejdetails.html')

@app.route('/saveDate.html')
def saveD():
    return send_from_directory('iPortfolio', 'saveDate.html')

@app.route('/siteweb.html')
def siteweb():
    return send_from_directory('iPortfolio', 'siteweb.html')

@app.route('/Sortie.html')
def sortie():
    return send_from_directory('iPortfolio', 'Sortie.html')

@app.route('/U.o.b2.html')
def uob():
    return send_from_directory('iPortfolio', 'U.o.b2.html')

""" # @app.route('/install.html')
# def designs():
#     return send_from_directory('iPortfolio', 'install.html') """

@app.route('/Ujaci.html')
def Ujaci():
    return send_from_directory('iPortfolio', 'Ujaci.html')

@app.route('/Uob.html')
def u_ob():
    return send_from_directory('iPortfolio', 'Uob.html')

@app.route('/Wedding.html')
def wedding():
    return send_from_directory('iPortfolio', 'Wedding.html')





@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Exécution du script PHP pour traiter le formulaire
        result = subprocess.run(['php', 'forms/contact.php', name, email, subject, message], capture_output=True, text=True)

        if result.returncode == 0:
            # Le traitement du formulaire avec PHP s'est terminé avec succès
            return 'Votre formulaire a été soumis avec succès.'
        else:
            # Une erreur s'est produite lors du traitement du formulaire avec PHP
            return 'Une erreur s\'est produite lors du traitement de votre formulaire.'
    else:
        # Méthode HTTP incorrecte
        return 'Méthode HTTP non autorisée.'

if __name__ == '__main__':
    app.run(host='192.168.43.128', port=8000)
