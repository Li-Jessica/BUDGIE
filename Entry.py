# SheHacks 2021 Submission
# Authors: Jessica Li, Rose Kim, Huiying Qin
# Description: class defining entry objects

import datetime

# class representing entry objects for csv data
class Entry:
    # constructor
    def __init__(self, category, cost):
        self.date = datetime.datetime.now()
        self.category = category
        self.cost = cost

