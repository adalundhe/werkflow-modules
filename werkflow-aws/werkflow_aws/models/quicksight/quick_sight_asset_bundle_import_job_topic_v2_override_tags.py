from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_tag import QuickSightTag


class QuickSightAssetBundleImportJobTopicV2OverrideTags(BaseModel):
    TopicIds: list[StrictStr] | None = None
    Tags: list[QuickSightTag] | None = None
