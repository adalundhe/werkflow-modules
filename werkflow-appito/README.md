# werkflow-appito

Version `0.2.0`

Asynchronous Apptio Frontdoor authentication and dataset upload module for [Werkflow](https://github.com/adalundhe/werkflow).

## Installation

```bash
pip install werkflow-appito
```

## Features

- **Werkflow `Module` Integration:** Zero-argument constructible `Appito(Module)` with async `close()` and sync `abort()`.
- **Frontdoor Authentication & Environment Lookup:** Exchanges Apptio API credentials (`AppitoCredentials`) for Frontdoor session tokens and resolves target environment details automatically.
- **Regional Endpoint Mapping (`AppitoRegionUrlMap`):** Supports US, EU, APAC, and GovCloud Apptio Frontdoor endpoints with safe fallback.
- **Dataset Uploads:** `upload_file()` validates local `.csv` and `.csv.gz` files and uploads them to the target Apptio table/period over `werkflow-http`.

## Usage

```python
from werkflow_appito import Appito, AppitoCredentials

creds = AppitoCredentials(
    appito_access_key="your-access-key",
    appito_secret_key="your-secret-key",
)

async with Appito() as appito:
    await appito.upload_file(
        credentials=creds,
        filepath="./costs.csv.gz",
        domain="example.com",
        project="Cloud Spend",
        table="AWS Billing",
    )
```

## Dependencies

- `werkflow-core`
- `werkflow-http`
- `werkflow-shell`
- `pydantic`

## Requirements

- Python `>=3.11`
