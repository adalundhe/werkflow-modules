from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetDataQualityModelRequest(BaseModel):
    ProfileId: StrictStr
    StatisticId: StrictStr | None = None
