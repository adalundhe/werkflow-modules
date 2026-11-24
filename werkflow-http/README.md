# werkflow-http

Version `0.7.0`

Asynchronous HTTP/1.1 client module for [Werkflow](https://github.com/adalundhe/werkflow) with connection pooling, async DNS resolution, TLS verification, cookies, redirects, and multipart file uploads.

## Installation

```bash
pip install werkflow-http
```

## Features

- **HTTP Verbs:** `get()`, `post()`, `put()`, `patch()`, `delete()`, `options()`, and `head()` with Pydantic v2 request validation (`Request`, `RequestWithData`, `HTTPRequest`).
- **Secure Defaults:** TLS certificate verification enabled by default (`HTTP(verify_ssl=True)`), with support for client certificates and HTTPS redirect upgrades.
- **Payloads & Multipart Uploads:** Automatic JSON serialization via `orjson` for dictionaries, lists, and Pydantic `BaseModel` payloads, plus async multipart file uploads via `File`.
- **Protocol Support:** Async DNS lookup via `aiodns`, query parameter encoding, cookie headers, chunked transfer decoding, and `204`/`304`/`HEAD` body handling.
- **Structured Responses (`HTTPResponse`):** Status code, headers, cookies, raw `content`, decoded `text`, and parsed JSON `data`.

## Usage

```python
from werkflow_http import HTTP, File

async with HTTP() as http:
    res = await http.get(
        "https://api.example.com/items",
        headers={"Accept": "application/json"},
        params={"limit": 10},
    )
    print(res.status, res.data)

    upload = await http.post(
        "https://api.example.com/upload",
        files=[File(path="./report.csv", name="file")],
    )
```

## Dependencies

- `werkflow-core`
- `aiodns`
- `orjson`
- `pydantic`

## Requirements

- Python `>=3.11`
