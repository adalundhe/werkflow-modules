from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .textract_blueprint_filter import TextractBlueprintFilter


class TextractListProjectsRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    BlueprintFilter: TextractBlueprintFilter | None = None
