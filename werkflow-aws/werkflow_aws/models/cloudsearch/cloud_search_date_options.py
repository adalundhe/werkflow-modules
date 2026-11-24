from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudSearchDateOptions(BaseModel):
    DefaultValue: StrictStr | None = None
    SourceField: StrictStr | None = None
    FacetEnabled: StrictBool | None = None
    SearchEnabled: StrictBool | None = None
    ReturnEnabled: StrictBool | None = None
    SortEnabled: StrictBool | None = None
