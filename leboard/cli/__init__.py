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
    2) Local file system (no shared options)
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
    try:
        import firebase_admin
        from firebase_admin import credentials
        from firebase_admin import firestore
    except:
        print("We could not find the firebase-admin package, install with `pip install firebase-admin`")

    cred = credentials.Certificate('firebase.json')
    default_app = firebase_admin.initialize_app(cred, name="leboard")






def local():
    """
    Set LocalHandler
    :return:
    """
    pass
