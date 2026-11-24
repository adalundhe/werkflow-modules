from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_custom_instructions import QuickSightCustomInstructions
from .quick_sight_topic_details import QuickSightTopicDetails


class QuickSightDescribeTopicResponse(BaseModel):
    Arn: StrictStr | None = None
    TopicId: StrictStr | None = None
    Topic: QuickSightTopicDetails | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    CustomInstructions: QuickSightCustomInstructions | None = None
    ResponseMetadata: dict[str, Any] | None = None
