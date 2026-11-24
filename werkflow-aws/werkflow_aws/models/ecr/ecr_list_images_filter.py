from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class ECRListImagesFilter(BaseModel):
    tagStatus: Literal['TAGGED', 'UNTAGGED', 'ANY'] | None = None
    imageStatus: Literal['ACTIVE', 'ARCHIVED', 'ACTIVATING', 'ANY'] | None = None
