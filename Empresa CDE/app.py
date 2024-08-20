from flask import Flask, render_template  # Importamos render_template

app = Flask(__name__)

@app.route('/')

def bienvenido():

   return render_template('principal.html')

if __name__=="__main__":

   app.run(debug=True)