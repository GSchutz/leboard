import leboard
import numpy as np


def test_leboard():

    letask = leboard.TaskBoard("__TEST_LEBOARD_TASK")
    # prevent error from any malformed test execution
    letask.delete()

    entries = {}

    for layer in range(1, 6):
        # run an experiment
        board_entry = letask.Entry()

        board_entry.set("accuracy", np.random.random())
        board_entry.set("loss", np.random.random() * 100)
        board_entry.set("layers", layer)

        # we can set dict like `layer_size: {first: 100, second: 200}`, add support for EntryData
        # board_entry.set("layer_size.first", 100)
        # board_entry.set("layer_size.second", 200)

        board_entry.commit()

        entries[board_entry.document.id] = board_entry.data.to_dict()

    # check if data is correctly added
    for snapshot in letask.collection.get():
        print(snapshot.to_dict())
        assert entries[snapshot.id] == snapshot.to_dict()

    for snap in letask.leaderboard("accuracy"):
        print(dict(id=snap.id, **snap.to_dict()))

    # clean space
    letask.delete()
