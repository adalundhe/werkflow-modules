from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KendraFeaturedResultsSetSummary(BaseModel):
    FeaturedResultsSetId: StrictStr | None = None
    FeaturedResultsSetName: StrictStr | None = None
    Status: StrictStr | None = None
    LastUpdatedTimestamp: StrictInt | None = None
    CreationTimestamp: StrictInt | None = None
