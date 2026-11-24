from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_custom_instructions import QuickSightCustomInstructions
from .quick_sight_topic_details import QuickSightTopicDetails


class QuickSightUpdateTopicRequest(BaseModel):
    AwsAccountId: StrictStr
    TopicId: StrictStr
    Topic: QuickSightTopicDetails
    CustomInstructions: QuickSightCustomInstructions | None = None
