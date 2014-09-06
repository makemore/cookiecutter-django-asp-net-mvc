cookiecutter-django-asp-net-mvc
==========================

A cookiecutter_ template for Django following what ASP.NET MVC gives you out of the box.

.. _cookiecutter: https://github.com/audreyr/cookiecutter

Description
-----------

It uses the latest stable versions and it only defines a skeleton which can be extended as needed.

Usage
------

Let's pretend you want to create a Django project called "redditclone". Rather than using `startproject`
and then editing the results to include your name, email, and various configuration issues that always get forgotten until the worst possible moment, get cookiecutter_ to do all the work.

First, get cookiecutter. Trust me, it's awesome::

Set up your virtualenv::

    $ cd <your-envs-folder>
    $ virtualenv  --no-site-packages redditclone
    $ cd redditclone
    $ source bin/activate
    $ pip install cookiecutter

Now run it against this repo::

    $ cd <your-workspace>
    $ cookiecutter  https://github.com/marcofucci/cookiecutter-simple-django.git

You'll be prompted for some questions, answer them, then it will create a Django project for you.


It prompts you for questions. Answer them::

    project_name (default is "project_name")? redditclone