#!/usr/bin/env python3
"""pymongo practice"""


def top_students(mongo_collection):
    """Returns all students sorted by their average score."""
    top_students = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
                }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_students
