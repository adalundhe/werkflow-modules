from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .awss3_inventory_configuration import AWSS3InventoryConfiguration


class AWSS3ListBucketInventoryConfigurationsResponse(BaseModel):
    ContinuationToken: StrictStr | None = None
    InventoryConfigurationList: list[AWSS3InventoryConfiguration] | None = None
    IsTruncated: StrictBool | None = None
    NextContinuationToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
