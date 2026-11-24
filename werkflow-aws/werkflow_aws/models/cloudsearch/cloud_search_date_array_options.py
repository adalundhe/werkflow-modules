from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudSearchDateArrayOptions(BaseModel):
    DefaultValue: StrictStr | None = None
    SourceFields: StrictStr | None = None
    FacetEnabled: StrictBool | None = None
    SearchEnabled: StrictBool | None = None
    ReturnEnabled: StrictBool | None = None
