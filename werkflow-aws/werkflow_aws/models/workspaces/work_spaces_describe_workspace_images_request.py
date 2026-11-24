from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class WorkSpacesDescribeWorkspaceImagesRequest(BaseModel):
    ImageIds: list[StrictStr] | None = None
    ImageType: Literal['OWNED', 'SHARED'] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
