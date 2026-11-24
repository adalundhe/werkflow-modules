from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightUpdateTopicResponse(BaseModel):
    TopicId: StrictStr | None = None
    Arn: StrictStr | None = None
    RefreshArn: StrictStr | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
