from api.config.logger import logger
import inspect

data = {
    "id": "problem3_oWqYc",
    "title": "Find the last index of the first occurrence word",
    "description": "",
    "timeLimit": 5,
    "input": ["words", "subword"],
    "testCase": {
        "1": {"words": "sadbutsad", "subword": "sad", "output": 2},
        "2": {"words": "hellolollo", "subword": "elo", "output": -1},
        "3": {"words": "interpretationinterpret", "subword": "pret", "output": 7},
    }
}