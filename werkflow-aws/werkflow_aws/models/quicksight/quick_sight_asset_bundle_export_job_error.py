from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAssetBundleExportJobError(BaseModel):
    Arn: StrictStr | None = None
    Type: StrictStr | None = None
    Message: StrictStr | None = None
