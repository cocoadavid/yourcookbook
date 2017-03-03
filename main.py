from flask import Flask, request, render_template, redirect, url_for, flash
from models import *
from init_database import InitDatabase
from example_recipes import *


app = Flask(__name__)


@app.route('/')
@app.route('/your_recipes', methods=['GET'])
def render_index():
    recipes = Food.select().order_by(Food.name.asc())
    return render_template('index.html', recipes=recipes)


@app.route('/starter_soup', methods=['GET'])
def render_starter():
    recipes = Food.select().where(Food.category == 'Starter/Soup').order_by(Food.name.asc())
    return render_template('index.html', recipes=recipes)


@app.route('/main_course', methods=['GET'])
def render_main_course():
    recipes = Food.select().where(Food.category == 'Main course').order_by(Food.name.asc())
    return render_template('index.html', recipes=recipes)


@app.route('/dessert', methods=['GET'])
def render_dessert():
    recipes = Food.select().where(Food.category == 'Dessert').order_by(Food.name.asc())
    return render_template('index.html', recipes=recipes)


@app.route('/search', methods=['POST'])
def render_search():
    recipes = Food.select().where(Food.name.contains(request.form['search']))
    return render_template('index.html', recipes=recipes)


@app.route('/add_new_recipe', methods=['GET'])
def render_new_recipe():
    recipe = []
    header = 'New recipe'
    button = 'Create recipe'
    return render_template('form.html', header=header, recipe=recipe, button=button)


@app.route('/recipe/<recipe_id>', methods=['GET'])
def render_edit_recipe(recipe_id):
    header = 'Edit recipe'
    recipe = Food.get(Food.id == recipe_id)
    button = 'Update recipe'
    return render_template('form.html', header=header, recipe=recipe, button=button)


@app.route('/show_recipe/<recipe_id>', methods=['GET'])
def show_recipe(recipe_id):
    recipe = Food.get(Food.id == recipe_id)
        
    return render_template('show_recipe.html', recipe=recipe)


@app.route('/recipe/', methods=['POST'])
def add_new_recipe():
    if request.form['image'] == '':
        img = 'default.jpg'
    else:
        img = request.form['image']

    ingr = request.form['ingredients']

    food = Food.create(     
        name=request.form['name'],
        ingredients=ingr,
        recipe=request.form['recipe'],
        category = request.form['category'],
        image=img
        )
    flash('New recipe was succesfully created!')
    return redirect(url_for('render_index'))


@app.route('/recipe/<recipe_id>', methods=['POST'])
def edit_recipe(recipe_id):
    update = Food.update(
        name=request.form['name'],
        ingredients=request.form['ingredients'],
        recipe=request.form['recipe'],
        category = request.form['category'],
        image=request.form['image']
        ).where(Food.id == recipe_id)

    update.execute()
    return redirect(url_for('render_index'))


@app.route('/delete/<recipe_id>', methods=['GET'])
def delete_recipe(recipe_id):
    story = Food.select().where(Food.id == recipe_id).get()
    story.delete_instance()
    story.save()
    return redirect(url_for('render_index'))





if __name__ == '__main__':
    InitDatabase.init_db()
    Generate.gen_data()
    app.secret_key = 'flashke'
    app.run(debug=True)