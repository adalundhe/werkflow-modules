from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_custom_instructions import QuickSightCustomInstructions
from .quick_sight_tag import QuickSightTag
from .quick_sight_topic_v2_details import QuickSightTopicV2Details


class QuickSightCreateTopicV2Request(BaseModel):
    AwsAccountId: StrictStr
    TopicId: StrictStr
    Topic: QuickSightTopicV2Details
    Tags: list[QuickSightTag] | None = None
    FolderArns: list[StrictStr] | None = None
    CustomInstructions: QuickSightCustomInstructions | None = None
