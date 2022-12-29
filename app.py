from flask import Flask, request, render_template, redirect
from convert import convert_file

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		# Get the file and the desired output format from the form
		file = request.files['file']
		input_format = file.filename.split('.')[-1]
		output_format = request.form['output_format']

		# Read the contents of the file
		file_contents = file.read()

		# Convert the file and get the output
		output = convert_file(input_format, output_format, file_contents)

		# Render the template with the output and the modified list of output formats
		# Check if there was an error during conversion
		if output == 'error':
			return redirect('/error')
		else:
			return render_template('convert.html', output=output, output_formats=['xml', 'yaml'])
	else:
		# Render the form template with the original list of output formats
		return render_template('form.html', output_formats=['xml', 'yaml'])

@app.route('/error')
def error():
	return render_template('error.html')

if __name__ == '__main__':
	app.run(debug=True)
