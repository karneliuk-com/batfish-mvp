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
    print("ANALYSIS // routes()")
    r1 = bfq.routes().answer().frame()
    print(r1)

    print("ANALYSIS // bgpRib()")
    r2 = bfq.bgpRib().answer().frame()
    print(r2)

    print("ANALYSIS // lpmRoutes()")
    r3 = bfq.lpmRoutes(ip='10.0.255.22').answer().frame()
    print(r3)

    # Saving output
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    r1.to_csv(f"{output_dir}/r1.csv")
    r2.to_csv(f"{output_dir}/r2.csv")
    r3.to_csv(f"{output_dir}/r3.csv")