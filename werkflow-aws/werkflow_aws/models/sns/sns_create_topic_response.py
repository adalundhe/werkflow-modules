from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SNSCreateTopicResponse(BaseModel):
    TopicArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
