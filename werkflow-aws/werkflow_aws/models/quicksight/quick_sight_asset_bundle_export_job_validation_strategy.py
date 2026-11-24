from __future__ import annotations
from pydantic import BaseModel, StrictBool


class QuickSightAssetBundleExportJobValidationStrategy(BaseModel):
    StrictModeForAllResources: StrictBool | None = None
