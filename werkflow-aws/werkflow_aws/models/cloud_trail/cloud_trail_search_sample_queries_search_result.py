from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class CloudTrailSearchSampleQueriesSearchResult(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    SQL: StrictStr | None = None
    Relevance: StrictFloat | StrictInt | None = None
