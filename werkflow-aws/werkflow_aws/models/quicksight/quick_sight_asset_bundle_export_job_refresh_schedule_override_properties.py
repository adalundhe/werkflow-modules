from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAssetBundleExportJobRefreshScheduleOverrideProperties(BaseModel):
    Arn: StrictStr | None = None
    Properties: list[StrictStr] | None = None
