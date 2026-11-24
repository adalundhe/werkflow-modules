from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .textract_project_filter import TextractProjectFilter


class TextractListBlueprintsRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    BlueprintArn: StrictStr | None = None
    ProjectFilter: TextractProjectFilter | None = None
    ResourceOwner: Literal['ACCOUNT', 'SERVICE'] | None = None
