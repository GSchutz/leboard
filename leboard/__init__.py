import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import pkg_resources

__version__ = pkg_resources.resource_stream(__name__, '../VERSION').read().decode('UTF-8')

FIREBASE_CREDENTIALS = 'firebase.json'


class Firebase:

    def __init__(self):
        self.credentials = credentials.Certificate(FIREBASE_CREDENTIALS)
        self.app = firebase_admin.initialize_app(self.credentials, name="leboard")

    def connect(self):
        self.client = firestore.client(self.app)


class TaskBoard:

    def __init__(self, name):
        self.storage = Firebase().connect()
        self.name = name
        self.collection = self.storage.collection(self.name)

    def Entry(self, **kwargs):
        return Entry(task=self, **kwargs)


class EntryData:
    def __init__(self, **kwargs):
        self._committed = False
        for k in kwargs:
            self.set(k, kwargs[k])

    def set(self, key, value):
        setattr(self, key, value)

    def to_dict(self):
        return self.__dict__


class Entry:

    def __init__(self, task: TaskBoard, **kwargs):
        """
        Set all entry (experiment) values at once
        :param kwargs:
        """
        self.committed = False
        self.task = task
        self.data = EntryData(**kwargs)
        # DocumentReference, for DocumentSnapshot use self.document.get()
        _, self.document = self.task.collection.add(self.data.to_dict())

    def set(self, key, value):
        # TODO should check the EntryType of value?
        self.data.set(key, value)
        self.document.update(self.data)

    def commit(self):
        self.committed = True
        self.data._committed = True
        self.document.update(self.data)


def task(name):
    """
    Create/Set a new Task Board
    """
    return TaskBoard(name)


