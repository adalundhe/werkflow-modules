from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightCreateTopicResponse(BaseModel):
    Arn: StrictStr | None = None
    TopicId: StrictStr | None = None
    RefreshArn: StrictStr | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
