from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectContactLensSummaryConfiguration(BaseModel):
    SummaryModes: list[StrictStr] | None = None
