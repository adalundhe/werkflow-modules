from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraBatchDeleteFeaturedResultsSetRequest(BaseModel):
    IndexId: StrictStr
    FeaturedResultsSetIds: list[StrictStr]
