from __future__ import annotations
from pydantic import BaseModel, StrictInt


class OpenSearchServerlessS3Statistics(BaseModel):
    objectsDiscovered: StrictInt | None = None
    objectsIngested: StrictInt | None = None
    objectsFailed: StrictInt | None = None
