cookiecutter-django-asp-net-mvc
==========================

A cookiecutter_ template for Django following what ASP.NET MVC gives you out of the box.

.. _cookiecutter: https://github.com/audreyr/cookiecutter

Description
-----------

The goal of this cookiecutter is to provide a solid starting point for a deployable app, without using magic or anticipating scaling (no redis backflips please).

- django 1.7
- bootstrap
- django-compressor
- example app that provides a homepage
- and crud scaffolding example (not ready)
- allauth (not ready)

Bare bone usage (sans virtual env, not recommended)
------

- install python https://www.python.org/download
- install pip http://pip.readthedocs.org/en/latest/installing.html
- sudo pip install cookiecutter
- cookiecutter https://github.com/makemore/cookiecutter-django-asp-net-mvc
- cd project_name

if postgres installed (recommended)

- sudo pip install -r requirements/dev.txt
- python manage runserver

else

- sudo pip install django
- python manage runserver

You should have an application good enough for production deployment running