from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_custom_instructions import QuickSightCustomInstructions
from .quick_sight_tag import QuickSightTag
from .quick_sight_topic_details import QuickSightTopicDetails


class QuickSightCreateTopicRequest(BaseModel):
    AwsAccountId: StrictStr
    TopicId: StrictStr
    Topic: QuickSightTopicDetails
    Tags: list[QuickSightTag] | None = None
    FolderArns: list[StrictStr] | None = None
    CustomInstructions: QuickSightCustomInstructions | None = None
