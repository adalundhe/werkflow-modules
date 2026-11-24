from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .msk_topic_info import MSKTopicInfo


class MSKListTopicsResponse(BaseModel):
    Topics: list[MSKTopicInfo] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
