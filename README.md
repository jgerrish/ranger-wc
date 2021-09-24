Word Count Plugin for Ranger
============================

A simple wordcount plugin to show number of lines in files in directory mode.

Tested with Ranger 1.9.3

Installation
============

Copy the directory to your ranger plugins directory:

cp -Ra ranger-wc ~/.config/ranger/plugins

Development
===========

To run tests:

pipenv install

PYTHONPATH=. pytests

Author
======

Joshua Gerrish
https://github.com/jgerrish/ranger-wc

