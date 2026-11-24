from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class QuickSightAssetBundleImportSource(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Body: StrictBytes | BinaryIO | StrictStr | None = None
    S3Uri: StrictStr | None = None
