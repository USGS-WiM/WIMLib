try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
setup(
    name='WiMpy',
    version='0.0.1',
    packages = ['src'],
    description='WiMPy is a custom reusable libraries and objects for handling geojson, logging, and other spatial operations leveraging ESRI ArGIS.',
    url='https://github.com/USGS-WiM/WiMPy',
    author='Jeremy K. Newson Web Informatics and Mapping',
    author_email='jknewson@usgs.gov',
    license='',
    install_requires=[
          'requests',
          'certifi'
      ]
     #dependency_links=['http://github.com/user/repo/tarball/master#egg=package-1.0']
    )



