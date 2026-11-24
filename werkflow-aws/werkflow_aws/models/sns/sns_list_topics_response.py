from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sns_topic import SNSTopic


class SNSListTopicsResponse(BaseModel):
    Topics: list[SNSTopic] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
