from __future__ import annotations
from pydantic import BaseModel, StrictInt


class DeviceFarmCounters(BaseModel):
    total: StrictInt | None = None
    passed: StrictInt | None = None
    failed: StrictInt | None = None
    warned: StrictInt | None = None
    errored: StrictInt | None = None
    stopped: StrictInt | None = None
    skipped: StrictInt | None = None
