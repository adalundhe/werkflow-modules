from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_tag import SageMakerTag


class SageMakerAddTagsResponse(BaseModel):
    Tags: list[SageMakerTag] | None = None
