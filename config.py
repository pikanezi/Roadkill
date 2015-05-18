import os
import jinja2

""" development active configuration (either "development" or "production") """
CONFIGURATION_TYPE = 'development' if os.environ.get('SERVER_SOFTWARE') == 'Development/2.0' else 'production'

""" jinja environment """
jinja_environment = jinja2.Environment(autoescape=True,
                                       loader=jinja2.FileSystemLoader(
                                           os.path.join(os.path.dirname(__file__), 'templates')))