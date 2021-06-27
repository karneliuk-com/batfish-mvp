#!/usr/bin/env python

# Modules
from pybatfish.client.commands import bf_init_snapshot, bf_session
from pybatfish.question.question import load_questions
from pybatfish.question import bfq
import os

# Variables
bf_address = "127.0.0.1"
snapshot_path = "./snapshots/nat"
output_dir = "./output"

# Body
if __name__ == "__main__":
    # Setting host to connect
    bf_session.host = bf_address

    # Loading confgs and questions
    bf_init_snapshot(snapshot_path, overwrite=True)
    load_questions()

    # Running questions
    r1 = bfq.unusedStructures().answer().frame()
    print(r1)

    r2 = bfq.undefinedReferences().answer().frame()
    print(r2)

    r3 = bfq.namedStructures().answer().frame()
    print(r3)

    r4 = bfq.definedStructures().answer().frame()
    print(r4)


    # Saving output
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    r1.to_csv(f"{output_dir}/r1.csv")
    r2.to_csv(f"{output_dir}/r2.csv")
    r3.to_csv(f"{output_dir}/r3.csv")
    r4.to_csv(f"{output_dir}/r4.csv")