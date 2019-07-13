import os
import time
import numpy as np
from bson.objectid import ObjectId

project = "test_warehouse"
local_storage = "./{}".format(project)

def generate_event(t):
    fname = str(ObjectId()) + ".pkl"
    element = np.random.choice(["Feature", "Label"], 1, p=[0.8, 0.2])[0]

    full = "/".join([local_storage, element, fname])
    cmd = "cp ./PCAAnimation.key {}".format(full)

    os.system(cmd)

    print("An {} at {}".format(element, t))

def generate_random_pause():
    error = np.random.normal(scale=5)

    error = max([error, -4.5])
    error = min([error, 3])

    return 5 + error

def get_p_from_time(t, fair_t):
    return t / (t + fair_t)

def randomly_stop(t, fair_t=120):
    p = get_p_from_time(t, fair_t)
    boo = np.random.choice([True, False], 1, p=[p, 1 - p])

    return boo

def signal_end():
    fname = "/".join([local_storage, "end"])

    f = open(fname, "w")
    f.close()
    print("end")


def test_case():
    start = time.time()
    t = 0

    while not randomly_stop(t, fair_t=20):
        generate_event(t)

        pause = generate_random_pause()
        time.sleep(pause)
        t = time.time() - start

    signal_end()


if __name__ == "__main__":
    test_case()
