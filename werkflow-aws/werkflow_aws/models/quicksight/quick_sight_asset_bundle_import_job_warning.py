from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAssetBundleImportJobWarning(BaseModel):
    Arn: StrictStr | None = None
    Message: StrictStr | None = None
