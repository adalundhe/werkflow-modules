from __future__ import annotations
from pydantic import BaseModel, StrictBool


class QuickSightAssetBundleExportJobResourceIdOverrideConfiguration(BaseModel):
    PrefixForAllResources: StrictBool | None = None
