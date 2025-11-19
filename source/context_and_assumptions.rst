=======================
Context and assumptions
=======================

About you
---------

I’m assuming you already have learnt the basics of Python. If you haven’t, a course like `Harvard’s CS50’s Introduction to Programming with Python <https://cs50.harvard.edu/python/>`_ would be a good starting point.

I’m trying hard **not** to assume other knowledge – it is a distinctive of these guides that they **don’t** assume you have a background in Computer Science, and they **don’t** assume knowledge of other programming languages or experience from a number of projects.

However, in a few cases, I’ll add notes for those who may be coming from another language and need to know the different way that Python works.


About your project
------------------

The lessons in this guide assume you are working on a project that uses modern Python, with a modern set of tools and practices.

This means:

- Python 3.12 or later. Most things will work with earlier versions of Python, but I’ll be using the most modern syntax available.

  If you are using an earlier version of Python, be aware of:

  - `What’s new in Python 3.12 <https://docs.python.org/3/whatsnew/3.12.html>`_
    - see “New typing features”
  - For a nice summary of the above, see Andy Pearce’s `What’s new in Python 3.12 - Type Hint Improvements <https://www.andy-pearce.com/blog/posts/2023/Dec/whats-new-in-python-312-type-hint-improvements/>`_

- You have an automated test suite.

- You will be using some kind of type checker like `mypy <https://mypy.readthedocs.io/en/stable/>`_, `pyright <https://github.com/microsoft/pyright>`_, or `basedpyright <https://docs.basedpyright.com/latest/>`_

- You are going to use the type checker in your automated tests.

- You are using some kind of modern editor or system that will provide immediate error checking feedback, preferably using the same type checker as above.

  My screen shots will be from Emacs, but you don’t have to use that. VS Code will be fine.
