import boto3

# from boto3 import ApplicationAutoScaling
import json

SCALING = boto3.client("application-autoscaling")
DIMENSION = {"read": "ReadCapacityUnits", "write": "WriteCapacityUnits"}


def get_scaleable_targets(table_name, dimension):
    return SCALING.describe_scalable_targets(
        ServiceNamespace="dynamodb",
        ResourceIds=["table/{}".format(table_name)],
        ScalableDimension="dynamodb:table:{}".format(DIMENSION[dimension]),
    )


def get_capacity(table_name, dimension):
    targets = get_scaleable_targets(table_name, dimension)["ScalableTargets"][0]
    return targets["MinCapacity"]


def scale(min_capacity, table_name, dimension):
    return SCALING.register_scalable_target(
        ServiceNamespace="dynamodb",
        ResourceId="table/{}".format(table_name),
        ScalableDimension="dynamodb:table:{}".format(DIMENSION[dimension]),
        MinCapacity=min_capacity,
    )

