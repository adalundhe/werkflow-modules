from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueSkewedInfo(BaseModel):
    SkewedColumnNames: list[StrictStr] | None = None
    SkewedColumnValues: list[StrictStr] | None = None
    SkewedColumnValueLocationMaps: dict[StrictStr, StrictStr] | None = None
