from __future__ import annotations
from pydantic import BaseModel, StrictBool


class QuickSightAssetBundleImportJobOverrideValidationStrategy(BaseModel):
    StrictModeForAllResources: StrictBool | None = None
