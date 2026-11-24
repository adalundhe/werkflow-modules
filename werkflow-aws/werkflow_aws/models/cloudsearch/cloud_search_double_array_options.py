from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class CloudSearchDoubleArrayOptions(BaseModel):
    DefaultValue: StrictFloat | StrictInt | None = None
    SourceFields: StrictStr | None = None
    FacetEnabled: StrictBool | None = None
    SearchEnabled: StrictBool | None = None
    ReturnEnabled: StrictBool | None = None
