## Sample worker
Sample worker depend on answers of crowdsourcing workers.
It answers by majority vote in matched answers.

## Requirments
- Install libraries by `pip install -r requirements.txt`
- You should set answer data at `answers/answered_facts_summary.csv`
- You should set params to `config.ini` (config example is `config.ini.sample`)

## Demonstration
```bash
python sample_worker.py
```
