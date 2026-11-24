from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class CloudSearchIntArrayOptions(BaseModel):
    DefaultValue: StrictInt | None = None
    SourceFields: StrictStr | None = None
    FacetEnabled: StrictBool | None = None
    SearchEnabled: StrictBool | None = None
    ReturnEnabled: StrictBool | None = None
