from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAssetBundleImportJobResourceIdOverrideConfiguration(BaseModel):
    PrefixForAllResources: StrictStr | None = None
