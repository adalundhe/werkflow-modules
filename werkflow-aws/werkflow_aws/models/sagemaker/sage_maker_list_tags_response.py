from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_tag import SageMakerTag


class SageMakerListTagsResponse(BaseModel):
    Tags: list[SageMakerTag] | None = None
    NextToken: StrictStr | None = None
