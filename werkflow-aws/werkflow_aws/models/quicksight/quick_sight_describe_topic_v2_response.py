from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_custom_instructions import QuickSightCustomInstructions
from .quick_sight_topic_v2_details import QuickSightTopicV2Details


class QuickSightDescribeTopicV2Response(BaseModel):
    Arn: StrictStr | None = None
    TopicId: StrictStr | None = None
    Topic: QuickSightTopicV2Details | None = None
    CustomInstructions: QuickSightCustomInstructions | None = None
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
