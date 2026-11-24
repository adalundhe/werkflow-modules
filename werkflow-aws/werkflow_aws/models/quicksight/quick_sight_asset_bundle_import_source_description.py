from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAssetBundleImportSourceDescription(BaseModel):
    Body: StrictStr | None = None
    S3Uri: StrictStr | None = None
