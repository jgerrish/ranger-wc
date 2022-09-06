Word Count Plugin for Ranger
============================

A simple wordcount plugin to show number of lines in files in directory mode.

The plugin is supposed to show some basic features of the ranger API.
In addition, it contains some useful pytest unit test patterns that
can be useful in other projects.

The project also contains a github workflow for pipenv to install
dependencies and run lints and tests.



Tested with Ranger 1.9.3

Installation
============

![python tests](https://github.com/jgerrish/ranger-wc/actions/workflows/python-package.yml/badge.svg)

Copy the directory to your ranger plugins directory:

cp -Ra ranger-wc ~/.config/ranger/plugins

Activate it by typing ":linemode wc" in ranger

Development
===========

To run tests:

pipenv install

pipenv run python -m pytest


To perform type checking with mypy:

mypy -m wc_linemode -m wc_helper --config-file mypy.ini


Author
======

Joshua Gerrish
https://github.com/jgerrish/ranger-wc

