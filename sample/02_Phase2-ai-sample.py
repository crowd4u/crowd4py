# -*- coding: utf-8 -*-
from utils.phases import *
from workers.ai_worker import AIWorker

if __name__ == "__main__":
    aiWorker = AIWorker(training=False)
    phase2(aiWorker, limit=1)
