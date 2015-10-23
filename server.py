from flask import Flask, render_template
from caldining import get_menu_items

app = Flask(__name__)

@app.route('/menu/<hall>')
def fetch_menu(hall):
	name = hall
	items = get_menu_items(6)
	return render_template('menu.html', items=items, name=name)

@app.route('/')
def home():
  return render_template('home.html')

if __name__ == '__main__':
  app.run(debug=True)
