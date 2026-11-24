from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .awss3_inventory_encryption import AWSS3InventoryEncryption


class AWSS3InventoryS3BucketDestination(BaseModel):
    AccountId: StrictStr | None = None
    Bucket: StrictStr | None = None
    Format: StrictStr | None = None
    Prefix: StrictStr | None = None
    Encryption: AWSS3InventoryEncryption | None = None
