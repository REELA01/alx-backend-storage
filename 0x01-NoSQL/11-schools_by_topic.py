#!/usr/bin/env python3
"""find by the topic"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """find by the topic"""
    return mongo_collection.find({"topics": topic})
