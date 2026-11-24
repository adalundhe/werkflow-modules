from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .awss3_inventory_configuration import AWSS3InventoryConfiguration


class AWSS3GetBucketInventoryConfigurationResponse(BaseModel):
    InventoryConfiguration: AWSS3InventoryConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
