from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraDescribeFeaturedResultsSetRequest(BaseModel):
    IndexId: StrictStr
    FeaturedResultsSetId: StrictStr
