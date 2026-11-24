from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_filter_value import BedrockFilterValue


class BedrockFilterAttribute(BaseModel):
    key: StrictStr | None = None
    value: BedrockFilterValue | None = None
