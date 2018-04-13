import os
import pkg_resources

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

__version__ = pkg_resources.resource_stream(__name__, 'VERSION').read().decode('UTF-8')

FIREBASE_CREDENTIALS = 'firebase.json'

query = firestore.firestore.Query

class Firebase:

    def __init__(self):

        if not os.path.isfile(FIREBASE_CREDENTIALS):
            raise FileNotFoundError("The firebase config file '{}' is required, you should run 'leboard init' for help "
                                    "with the initial setup.".format(FIREBASE_CREDENTIALS))

        self.credentials = credentials.Certificate(FIREBASE_CREDENTIALS)
        self.app = firebase_admin.initialize_app(self.credentials, name="leboard")

    def connect(self):
        self.connection = firestore.client(self.app)
        return self


class TaskBoard:

    def __init__(self, name):
        self.storage = Firebase().connect().connection
        self.name = name
        self.collection = self.storage.collection(self.name)

    def Entry(self, **kwargs):
        return Entry(task=self, **kwargs)

    def leaderboard(self, rank_field, direction=query.DESCENDING):
        return self.collection.order_by(rank_field, direction=direction).get()

    def delete(self):
        batch_size = 100
        docs = self.collection.limit(batch_size).get()
        deleted = 0

        for doc in docs:
            print('Deleting doc {} => {}'.format(doc.id, doc.to_dict()))
            doc.reference.delete()
            deleted += 1

        if deleted >= batch_size:
            return self.delete()


class EntryData:
    def __init__(self, **kwargs):
        self._committed = False
        for k in kwargs:
            self.set(k, kwargs[k])

    def set(self, key, value):
        # TODO add subpaths support, like "field.subfield": "value"
        # like, reduce(lambda x, y: {y: x}, reversed(key.split(".")), value)
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
        self.data = EntryData(_count=sum(1 for _ in self.task.collection.get()), **kwargs)
        # DocumentReference, for DocumentSnapshot use self.document.get()
        _, self.document = self.task.collection.add(self.data.to_dict())

    def set(self, key, value):
        # TODO should check the EntryType of value?
        self.data.set(key, value)
        self.document.update(self.data.to_dict())

    def commit(self):
        self.committed = True
        self.data._committed = True
        self.document.update(self.data.to_dict())


def task(name):
    """
    Create/Set a new Task Board
    """
    return TaskBoard(name)


