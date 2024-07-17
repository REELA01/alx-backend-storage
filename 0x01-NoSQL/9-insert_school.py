#!/usr/bin/env python3
"""the module have a utility function that insert documents"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """insert in to school"""
    return mongo_collection.insert_one(kwargs).inserted_id
