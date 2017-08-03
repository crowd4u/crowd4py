# Worker examples
- Human worker
- Sample worker

## Human worker
The example of Human worker simulates behaviors for human. It depends on data of crowdsoursing workers.

## Sample worker
The exmample of sample worker answers by majority vote by answers data. Therefore it depends on data of crowdsourcing workers.

## Requirments
- Install libraries by `pip install -r requirements.txt`
- You should set answer data at `answers/answered_facts_summary.csv`
- You should set params to `config.ini` (config example is `config.ini.sample`)

## Demonstration
```bash
python *_worker.py
```
