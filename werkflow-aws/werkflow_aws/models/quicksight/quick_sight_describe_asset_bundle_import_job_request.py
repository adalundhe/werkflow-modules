from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeAssetBundleImportJobRequest(BaseModel):
    AwsAccountId: StrictStr
    AssetBundleImportJobId: StrictStr
