from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class CloudSearchDoubleOptions(BaseModel):
    DefaultValue: StrictFloat | StrictInt | None = None
    SourceField: StrictStr | None = None
    FacetEnabled: StrictBool | None = None
    SearchEnabled: StrictBool | None = None
    ReturnEnabled: StrictBool | None = None
    SortEnabled: StrictBool | None = None
