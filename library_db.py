# library_db
# Fill out a form to query the library database

# By stringzzz, Ghostwarez Co.
# 09-19-2025

from flask import Flask, render_template, request # type: ignore
app = Flask(__name__)

def mysql_run_query(inputs):
	import mysql.connector # type: ignore
	from mysql.connector import errorcode # type: ignore

	query_output = []
	final_output = ""

	try:

		# Connect to local database
		my_db = mysql.connector.connect(
			user='Librarian',
			password='********',
			host='localhost',
			database='library_db'
		)

		my_cursor = my_db.cursor()

		#Build query:
		filters = []
		no_filters = True

		#Title
		if inputs['title_search'] != 'Any':
			if inputs['title_search_type'] == 'full':
				filters.append(f"Title = '{inputs['title_search']}'")
			elif inputs['title_search_type'] == 'partial':
				filters.append(f"Title LIKE '%{inputs['title_search']}%'")

		#Author
		if inputs['author_search'] != 'Any':
			if inputs['author_search_type'] == 'full':
				filters.append(f"Author = '{inputs['author_search']}'")
			elif inputs['author_search_type'] == 'partial':
				filters.append(f"Author LIKE '%{inputs['author_search']}%'")
		
		#Genres
		if len(inputs['genres']) != 0:
			genres_strings = []
			for genre in inputs['genres']:
				genres_strings.append(f"'{genre}'")
			filters.append(f"Genre IN ({", ".join(genres_strings)})")

		#Minimum year published
		if inputs['min_publication'] != '0':
			filters.append(f"Year_Published >= {inputs['min_publication']}")

		#Maximum year published
		if inputs['max_publication'] != '3000':
			filters.append(f"Year_Published <= {inputs['max_publication']}")

		#Minimum pages
		if inputs['min_pages'] != '0':
			filters.append(f"Pages >= {inputs['min_pages']}")

		#Maximum pages
		if inputs['max_pages'] != '9999':
			filters.append(f"Pages <= {inputs['max_pages']}")

		#Check if filters added
		if len(filters) != 0:
			no_filters = False

		#Build the final query string
		query_string = ""
		if no_filters:
			query_string = f"SELECT {", ".join(inputs['output_columns'])} FROM Books ORDER BY {inputs['sort_by_column']} {inputs['sort_by_type']};"
		else:
			query_string = f"SELECT {", ".join(inputs['output_columns'])} FROM Books WHERE {" AND ".join(filters)} ORDER BY {inputs['sort_by_column']} {inputs['sort_by_type']};"

		# #Debug
		# print(query_string)

		my_cursor.execute(query_string)

		# Get the column names from the query
		if my_cursor.description:
			column_names = [i[0] for i in my_cursor.description]
		temp_output = [column_names[:]] # For clarity

		# Get the results of the query
		my_result = my_cursor.fetchall()
		for x in my_result:
			query_output.append(x)

		# Add results rows from the query to a list with the columns at the beginning
		for row in query_output:
			temp_output.append(list(row))

		final_output = temp_output

	# Handle any errors

	except(mysql.connector.errors.ProgrammingError) as err:
		final_output = f"Programming Error: {err}"

	except(mysql.connector.errors.OperationalError) as err:
		final_output = f"Operational Error: {err}"

	except(mysql.connector.errors.Error) as err:
		final_output = f"General MySQL Error: {err}"

	# Cleanup

	finally:
		my_cursor.close()
		my_db.close()

	return final_output

@app.route('/', methods=['GET', 'POST'])
def web_page_io():

	if request.method == 'POST':

		#Create dictionary for form inputs
		inputs = {
			'title_search': "",
			'title_search_type': "",
			'author_search': "",
			'author_search_type': "",
			'genres': [],
			'min_publication': "",
			'max_publication': "",
			'min_pages': "",
			'max_pages': "",
			'output_columns': []
		}

		#Grab the various inputs from the form
		inputs['title_search'] = request.form['title-search']
		inputs['title_search_type'] = request.form['title-search-type']
		inputs['author_search'] = request.form['author-search']
		inputs['author_search_type'] = request.form['author-search-type']
		inputs['genres'] = request.form.getlist('genre-selection')
		inputs['min_publication'] = request.form['min-publication']
		inputs['max_publication'] = request.form['max-publication']
		inputs['min_pages'] = request.form['min-pages']
		inputs['max_pages'] = request.form['max-pages']
		inputs['sort_by_column'] = request.form['sort-by-column']
		inputs['sort_by_type'] = request.form['sort-by-type']		
		inputs['output_columns'] = request.form.getlist('output-columns')

		# #Debug
		# for k in inputs.keys():
		# 	print(inputs[k])

		return render_template('library_db.html', table_data=mysql_run_query(inputs))

	return render_template('library_db.html')

# Allow access from any IP address.
# !!! DON'T allow port forwarding on router, else anyone outside can access it!
if __name__ == "__main__":
	app.run('0.0.0.0', port=5000, debug=True)
