"""
leboard

Usage:
    leboard init
"""

from docopt import docopt

from leboard import __version__


def main():
    """Main CLI entrypoint."""
    options = docopt(__doc__, version=__version__)

    commands = globals()

    for k, v in options.items():
        if k in commands:
            commands[k](options)


def init(p):
    print("Initializing leboard")

    handlers = {"1": {"name": "Google Firebase", "init": firebase},
                "2": {"name": "Local file system", "init": local}}

    handler = input("""Choose an option for Data Handler (1):
    1) Google Firebase (recommended)
    2) Local file system (not supported yet)
    """)

    if handler not in handlers:
        print("No option for {}".format(handler))
        return init(p)

    print("You choose {}".format(handlers[handler]["name"]))
    handlers[handler]["init"]()


def firebase():
    """
    Set FirebaseHandler
    :return:
    """
    print("""
    Please, follow this steps:
     1) Create a Firebase project at https://console.firebase.google.com/.
     2) Access the page Firebase Database and activate the Firestore database.
     3) Generate a key for the App Engine (gcloud credential) at https://console.cloud.google.com/iam-admin/serviceaccounts/project (for your created project).
     4) Download the json file and save in 'firebase.json'.
    """)


def local():
    """
    Set LocalHandler
    :return:
    """
    pass
