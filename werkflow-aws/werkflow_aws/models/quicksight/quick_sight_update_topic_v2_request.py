from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .quick_sight_custom_instructions import QuickSightCustomInstructions
from .quick_sight_topic_v2_details import QuickSightTopicV2Details


class QuickSightUpdateTopicV2Request(BaseModel):
    AwsAccountId: StrictStr
    TopicId: StrictStr
    Topic: QuickSightTopicV2Details
    CustomInstructions: QuickSightCustomInstructions | None = None
    PublishOption: Literal['DRAFT', 'PUBLISH'] | None = None
