from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class RekognitionDescribeProjectsRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    ProjectNames: list[StrictStr] | None = None
    Features: list[Literal['CONTENT_MODERATION', 'CUSTOM_LABELS']] | None = None
