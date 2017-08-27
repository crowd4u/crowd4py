# Worker Examples
the worker examples are in workers directories.
- Algorithm Worker
- Machine Learning Worker

## Algorithm Worker
The worker works by simple human rulebase. When book's title is matched, the worker answer correct state.

## Machine Learning Worker[WIP]
The worker works by a machine learning model.

## Requirments
1. Install libraries by `pip install -r requirements.txt`
2. You should set params to `config.ini` (config example is in `config.ini.sample`)

## Demonstration

### Learning phase demonstration
```bash
python Phase1-algorithm-sample.py
```

### Anseering phase demonstration
```bash
python Phase2-algorithm-sample.py
```

# Create Worker
Crowd4py and those util methods already implement useful interface, So you only implement worker behaviors.

## Implement Workers
The worker implementing needs to inherite WorkerBase class.
The WorkerBase class is following that.

```python
class WorkerBase():
    def train(self, ...):
    def output(self, ...):
```

So we implement train method and output method for creating worker.

The train method create training models if you implementing machine learning based worker.
Or, if you create human rule based worker, you do not implement train method.

Second, the output method create worker answering.
The answering must return True or False.
