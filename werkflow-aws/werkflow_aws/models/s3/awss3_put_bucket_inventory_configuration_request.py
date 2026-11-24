from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .awss3_inventory_configuration import AWSS3InventoryConfiguration


class AWSS3PutBucketInventoryConfigurationRequest(BaseModel):
    Bucket: StrictStr
    Id: StrictStr
    InventoryConfiguration: AWSS3InventoryConfiguration
    ExpectedBucketOwner: StrictStr | None = None
