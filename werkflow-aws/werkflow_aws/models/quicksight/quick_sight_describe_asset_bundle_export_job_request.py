from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeAssetBundleExportJobRequest(BaseModel):
    AwsAccountId: StrictStr
    AssetBundleExportJobId: StrictStr
