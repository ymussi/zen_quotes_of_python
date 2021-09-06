from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='zen_quotes',
    version = '1.1.3',
    author='Yuri Mussi',
    author_email='ymussi@gmail.com',
    description='A list Zen of Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    setup_requires=["setuptools-git-version"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules='zen_quotes',
    package_dir={'':'zen/quotes'},
    license='BSD',
    url='https://github.com/ymussi/zen_quotes_of_python',
    keywords = "Mussi",
    install_requires = ['configparser==3.5.0'],
    zip_safe=False
    ),