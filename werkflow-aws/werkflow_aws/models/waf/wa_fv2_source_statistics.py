from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class WAFv2SourceStatistics(BaseModel):
    SourceName: StrictStr | None = None
    Percentage: StrictFloat | StrictInt | None = None
    Amount: StrictStr | None = None
    RequestCount: StrictInt | None = None
    SourceCategory: StrictStr | None = None
    Intent: StrictStr | None = None
    Organization: StrictStr | None = None
    Verified: StrictBool | None = None
    GroupByValue: StrictStr | None = None
