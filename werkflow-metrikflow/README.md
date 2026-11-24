# werkflow-metrikflow

Version `0.3.0`

Asynchronous [Metrikflow](https://github.com/adalundhe/metrikflow) metrics publishing and loading module for [Werkflow](https://github.com/adalundhe/werkflow).

## Installation

```bash
pip install werkflow-metrikflow
```

## Features

- **Optional Dependency Safe:** Imports cleanly even when the optional `metrikflow` runtime is not installed (`Metrik.module_enabled = False`, raising `MissingModuleError` on instantiation or `@requires(Metrik)` validation).
- **Senders & Loaders:** `connect_sender()` and `connect_loader()` connect to configured Metrikflow backends asynchronously.
- **Metric Operations:** `record_metric()`, `send_metric()` (with metric `unit`, `Event`, `Interval`, and `Rate` support), and `load_metric()`.
- **Async Lifecycle:** Properly shuts down connected senders/loaders in `await metrik.close()` and `metrik.abort()`.

## Usage

```python
from werkflow_metrikflow import Metrik

async with Metrik() as metrik:
    await metrik.connect_sender(sender_type="prometheus", config={...})
    await metrik.send_metric(
        name="deploy_duration_seconds",
        value=12.4,
        unit="seconds",
    )
```

## Dependencies

- `werkflow-core`
- `werkflow-shell`
- `metrikflow`

## Requirements

- Python `>=3.11`
