# -*- coding: utf-8 -*-
from utils.phases import *
from workers.ai_worker import AIWorker

if __name__ == "__main__":
    aiWorker = AIWorker(training=True)
    phase1(aiWorker, limit=5)

    print("---AIWorker Fitting---")
    aiWorker.fit()

    print("---AIWorker Dumping---")
    aiWorker.dump()
