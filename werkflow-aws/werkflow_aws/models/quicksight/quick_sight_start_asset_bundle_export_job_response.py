from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightStartAssetBundleExportJobResponse(BaseModel):
    Arn: StrictStr | None = None
    AssetBundleExportJobId: StrictStr | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
