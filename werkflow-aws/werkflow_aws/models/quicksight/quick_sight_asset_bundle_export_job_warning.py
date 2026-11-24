from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAssetBundleExportJobWarning(BaseModel):
    Arn: StrictStr | None = None
    Message: StrictStr | None = None
