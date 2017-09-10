# Worker Examples
the worker examples are in workers directories.
- Algorithm Worker
- Machine Learning Worker

## Algorithm Worker
The worker works by simple human rulebase. When book's title is matched, the worker answer correct state.

## Machine Learning Worker
The worker works by a machine learning model by SVM.

## Requirments
1. Install libraries by `pip install -r requirements.txt`
2. You should set params to `config.ini` (config example is in `config.ini.sample`)

## Demonstration

### Learning phase demonstration
```bash
python Phase1-algorithm-sample.py
```

### Answering phase demonstration
```bash
python Phase2-algorithm-sample.py
```

# Create Worker
The process of worker sample is following that.

```python
worker = Worker()
api = API(config)

# Phase1: training phase
for i in range(phase1_limit):
    book1, book2, result = api.fetchTrainingData()
    Worker.train(book1, book2, result)

# Phase2: predict phase
for i in range(phase2_limit):
    book1, book2 = api.fetchData()
    answer = algorithmWorker.predict(book1, book2)
    api.send(answer)
```

api class is used by utils/api.py, so we only implement worker class.

## Implement Workers Example
The WorkerBase class is following that.

```python
class WorkerBase():
    def train(self, book1, book2, result):
    def predict(self, book1, book2): return True or False
```

So we implement train method and predict method for creating worker.

The train method create training models if you implementing machine learning based worker.
Or, if you create human rule based worker, you do not implement train method.

Second, the predict method create worker answering.
The worker answering must return True or False.
