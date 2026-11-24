from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class RekognitionCreateProjectRequest(BaseModel):
    ProjectName: StrictStr
    Feature: Literal['CONTENT_MODERATION', 'CUSTOM_LABELS'] | None = None
    AutoUpdate: Literal['ENABLED', 'DISABLED'] | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
