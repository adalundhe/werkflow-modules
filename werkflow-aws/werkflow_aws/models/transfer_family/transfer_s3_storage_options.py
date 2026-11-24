from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferS3StorageOptions(BaseModel):
    DirectoryListingOptimization: StrictStr | None = None
