from __future__ import annotations
from pydantic import BaseModel
from .awss3_inventory_s3_bucket_destination import AWSS3InventoryS3BucketDestination


class AWSS3InventoryDestination(BaseModel):
    S3BucketDestination: AWSS3InventoryS3BucketDestination | None = None
