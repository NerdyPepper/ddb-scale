import boto3

# from boto3 import ApplicationAutoScaling
import json
import argparse
import sys
from .util import *

DESCRIPTION = "Scale up/down any dimension of a DynamoDB table"


def main():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(
        "-m",
        "--min-capacity",
        default=5,
        dest="capacity",
        help="modified min capacity",
        metavar="CAPACITY",
        required=True,
        type=int,
    )
    parser.add_argument(
        "-d",
        "--dimension",
        choices=["read", "write"],
        dest="dimension",
        help="dimension to scale",
        required=True,
        type=str,
    )
    parser.add_argument(
        "table", metavar="TABLE", help="name of DynamoDB table", type=str
    )

    args = parser.parse_args()

    dimension = args.dimension
    table = args.table
    capacity = args.capacity

    try:
        existing_capacity = get_capacity(table, dimension)
        print(
            "Current {} capacity for {} ... {} units".format(
                dimension, table, existing_capacity
            )
        )

        print(
            "Scaling {} capacity for {} to  {} units".format(dimension, table, capacity)
        )
        scale(capacity, table, dimension)

        print("Done!")

    except (IndexError, KeyError):
        print("Invalid table name or authentication key!")
        print("Exiting ...")
        sys.exit()
