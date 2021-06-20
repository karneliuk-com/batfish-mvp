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
    r = bfq.nodeProperties().answer().frame()
    print(r)

    # Saving output
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    r.to_csv(f"{output_dir}/results.csv")