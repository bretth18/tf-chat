

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'tf_chatbot',
    'author': 'bretth18',
    'url': 'null',
    'download_url': 'null',
    'author_email': 'bretth18@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['tensorflow'],
    'scripts': [],
    'name': 'tensorflowchatbot'
}

setup(**config)
