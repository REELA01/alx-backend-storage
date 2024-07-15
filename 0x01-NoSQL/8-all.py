#!/usr/bin/env python3
"""The module have a utility function that list all document"""
import pymongo


def list_all(mongo_collection):
    """list all collection"""
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
