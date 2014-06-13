from setuptools import setup, find_packages
from geojson_tiles import __version__

README = open('README.rst').read()

setup(name='django-geojson-tiles',
      version=__version__,
      description='GeoJSON tile view for Django',
      long_description=README,
      author='Glen Robertson',
      author_email='robertson.glen@gmail.com',
      packages=find_packages(),
      include_package_data=True,
      install_requires=['django', 'Pillow', 'ModestMaps==1.4.6', 'TileStache==1.40.1'],
)
