from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftConnect(BaseModel):
    Authorization: StrictStr | None = None
