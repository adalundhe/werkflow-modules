from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .cloud_front_encryption_entity import CloudFrontEncryptionEntity


class CloudFrontEncryptionEntities(BaseModel):
    Quantity: StrictInt | None = None
    Items: list[CloudFrontEncryptionEntity] | None = None
