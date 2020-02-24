from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='zen_of_python',
    # other arguments omitted
    long_description=long_description,
    long_description_content_type='text/markdown',
    version = '0.0.1',
    setup_requires=["setuptools-git-version"],
    packages = find_packages(),
    description='A list Zen of Python',
    author='Yuri Mussi',
    author_email='ymussi@gmail.com',
    license='BSD',
    url='https://github.com/ymussi/zen_of_python',
    keywords = "Mussi",
    install_requires = ['gunicorn<=20',
                        'flask==1.0.2',
                        'flask-restplus',
                        'configparser==3.5.0',
                        'requests==2.18.4',
                        'flask_cors',
                        'flask_accepts==0.15.5',
                        'werkzeug==0.16.1'],
    zip_safe=False
    ),