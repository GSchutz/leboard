# Le Board

Le Board, a simple leaderboard generator for ranking your
algorithms experiments.



# Install

Install with `pip` and configure with `init`, linking a Google
account is the recommended choice.

```
pip install leboard

leboard init
```

## sketch of `leboard init`
> Choose an option for Data Handler (1):
> 1) Google Firebase (recommended)
> 2) Local file system (no shared options)

## if option 1)
> Choose a name for Firebase project (leboard):

## if option 2)
> Choose a path to store your board (~/.leboard):



# Usage

```
import leboard

leboard.task("MNIST")

# other members will have access to the MNIST task too
# (restrict a members definition only when a task is set)
leboard.members(["rob@gmail.com", "jane@mail.com"])

# do your stuff
# ...

experiment = leboard.Entry()

experiment.add("accuracy", accuracy)
experiment.add("loss", loss)
experiment.add("parameters", params, hide=True)
experiment.add("confusion_image", confusion_image)

# commit will save to DataHandles available/configured
# (proposed is local simple file storage, and shared google firebase)
experiment.commit()
```


##  Leaderboard

Show all experiments with links to detailed resources,
this can open a page hosted in firebase.

- keep experiment data in order of creation

```
import leboard

leboard.set_rank("accuracy", "ASC")

leboard.leaderboard("MNIST")
```


# Advanced?

## Resource Typing?

Entry can have different types, this can be usefull for
handling resources like image, or HTML pages, to show and
interact with them.

```
import leboard
from leboard import types as lbt

experiment = leboard.Entry()

experiment.add("accuracy", accuracy)
experiment.add("loss", loss)
experiment.add("confusion_image", lbt.Image(confusion_image))
experiment.add("notebook_html", lbt.HTML(notebook_html))
```

Committing an `Entry` could automatically save a copy of
the current notebook state to the DataHandler.