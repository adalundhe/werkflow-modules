from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class GlueGetCatalogsRequest(BaseModel):
    ParentCatalogId: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    Recursive: StrictBool | None = None
    IncludeRoot: StrictBool | None = None
    HasDatabases: StrictBool | None = None
