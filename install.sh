#/bin/bash

python -m pip install --user --upgrade setuptools wheel

python setup.py sdist bdist_wheel

pip install -e .
