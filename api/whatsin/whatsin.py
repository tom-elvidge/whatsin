from urllib import response
import numpy
from flask import (
    Blueprint, flash, g, jsonify, redirect, render_template, request, session, url_for
)
from whatsin.db import get_db


bp = Blueprint('whatsin', __name__, url_prefix='/whatsin')

SQL_TEMPLATE = '''
            SELECT ingredient
            FROM RecipeIngredients
            WHERE recipe_id IN (
                SELECT id FROM Recipes
                WHERE title LIKE '%{}%'
            );
        '''


@bp.route('/<string:query>', methods=['GET'])
def update(query):
    # Use ' ' for spaces.
    query = query.replace('%20', ' ')
    query = query.replace('+', ' ')

    # The query is allowed to contain alphabetic characters or spaces.
    # If it contains anything else raise an exception in case SQL injection.
    if not query.replace(' ', '').isalpha():
        raise Exception('query contains illegal characters.')

    # Replace spaces with % to allow any characters between the words in query.
    sql = SQL_TEMPLATE.format(query.replace(' ', '%'))

    # Execute sql on database.
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute(sql)

    # Extract all ingredients from SQL query response.
    ingredients = []
    for m in cursor.fetchall():
        ingredients.append(m['ingredient'])

    # Get the frequency of each ingredient.
    ingredient_frequencies = get_frequencies(ingredients)
    
    # Filter to get all the ingredients with a high relative frequency.
    generic_ingredients = filter_ingredients(ingredient_frequencies, 1.5)
    
    # Create response.
    body = {
        'ingredients': generic_ingredients
    }
    response = jsonify(body)


    # Allow CORS.
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


def get_frequencies(ingredients):
    '''
    Count the number of occurences of each word or phrase in the passed list of ingredients.
    
    Parameters:
        ingredients - list - A list of ingredients. Each ingredient may occur many times.
    
    Returns:
        dict - A dictionary mapping each unique ingredient in words to the number of occurences.
    '''
    frequency = {}

    # Update frequency for each word.
    for ingredient in ingredients:
        # Dictionary keys must be immutable, so wrap in tuple.
        if ingredient in frequency:
            frequency[ingredient] = frequency[ingredient] + 1
        else:
            frequency[ingredient] = 1

    return frequency


def filter_ingredients(frequencies, std_scale):
    '''
    Filter the ingredients in ingredient_frequencies to get only the frequent ingredients.
    
    The frequency must be greater than the median + (std * std_scale).
    
    Parameters:
        frequencies - dict - A mapping of ingredients to their frequencies.
        std_scale - float - Scale the standard deviation. The greater this is the stricter the filter.
    
    Returns:
        list - A list of the ingredients that passed the filter.
    '''
    # Calculate median and standard deviation of the ingredient frequencies.
    med = numpy.median(list(frequencies.values()))
    std = numpy.std(list(frequencies.values()))
     
    # Get all the ingredients which have a frequency greater than med + (std * std_scale)
    passed = []
    for ingredient in frequencies.keys():
        if frequencies[ingredient] > med + (std * std_scale):
            passed.append(ingredient)

    return passed