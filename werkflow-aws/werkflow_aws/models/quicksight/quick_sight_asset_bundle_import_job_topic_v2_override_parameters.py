from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAssetBundleImportJobTopicV2OverrideParameters(BaseModel):
    TopicId: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
