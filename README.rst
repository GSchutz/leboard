Le Board (beta)
===============

Le Board, a simple leaderboard generator for ranking your
algorithms experiments.

Install
=======

Install with ``pip`` and configure with ``init``, linking a Google
account is the recommended choice.

.. code-block:: bash

    $ pip install leboard
    $ leboard init

sketch of ``leboard init``
------------------------------

..

Choose an option for Data Handler (1):

1) Google Firebase (recommended)
2) Local file system (no shared options)


if option 1)
------------

..

* Create a Firebase project at https://console.firebase.google.com/
* Get the gcloud credential at https://console.cloud.google.com/iam-admin/serviceaccounts/project
* Access the page Database -> activate the Firestore database


if option 2)
------------

..

* Choose a path to store your boards (~/.leboard):


Usage
=====

.. code-block:: python

    import leboard
    
    letask = leboard.TaskBoard("MNIST")
    
    # other members will have access to the MNIST task too
    # (restrict a members definition only when a task is set)
    letask.members(["rob@gmail.com", "jane@mail.com"])
    
    # do your stuff
    # ...
    
    experiment = letask.Entry()
    
    experiment.set("accuracy", accuracy)
    experiment.set("loss", loss)
    experiment.set("parameters", params, hide=True)
    experiment.set("confusion_image", confusion_image)
    
    # commit will save to DataHandler available/configured
    # (proposed is local simple file storage, and shared google firebase)
    experiment.commit()
    
Leaderboard
-----------

Show all experiments with links to detailed resources,
this can open a page hosted in firebase.


* keep experiment data in order of creation

.. code-block:: python

    letask.leaderboard("MNIST", "accuracy")

Advanced?
=========

Resource Typing?
----------------

Entry can have different types, this can be usefull for
handling resources like image, or HTML pages, to show and
interact with them.

.. code-block:: python

    from leboard import types as lbt
    
    experiment.set("accuracy", accuracy)
    experiment.set("loss", loss)
    experiment.set("confusion_image", lbt.Image(confusion_image))
    experiment.set("notebook_html", lbt.HTML(notebook_html))
    

Committing an ``Entry`` could automatically save a copy of
the current notebook state to the ``DataHandler``.
