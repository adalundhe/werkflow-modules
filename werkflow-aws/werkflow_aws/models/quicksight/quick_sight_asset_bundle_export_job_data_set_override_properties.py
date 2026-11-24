from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAssetBundleExportJobDataSetOverrideProperties(BaseModel):
    Arn: StrictStr | None = None
    Properties: list[StrictStr] | None = None
