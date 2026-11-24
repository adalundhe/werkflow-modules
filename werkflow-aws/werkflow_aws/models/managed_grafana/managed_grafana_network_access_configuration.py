from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedGrafanaNetworkAccessConfiguration(BaseModel):
    prefixListIds: list[StrictStr] | None = None
    vpceIds: list[StrictStr] | None = None
