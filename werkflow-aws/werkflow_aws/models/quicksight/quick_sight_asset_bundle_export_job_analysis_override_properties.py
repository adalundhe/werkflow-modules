from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAssetBundleExportJobAnalysisOverrideProperties(BaseModel):
    Arn: StrictStr | None = None
    Properties: list[StrictStr] | None = None
