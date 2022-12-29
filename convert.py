import yaml
import xmltodict

def convert_file(input_format, output_format, file_contents):
	try:
		# Convert the file to the desired output format
		if output_format == 'xml':
			data = yaml.safe_load(file_contents)
			output = xmltodict.unparse(data, pretty=True)
	
		if output_format == 'yaml':
			data = xmltodict.parse(file_contents)
			output = yaml.dump(data, default_flow_style=False)
		
		#if output_format == 'csv':
			
	
	except:
		output='error'
	
	
	return output
	