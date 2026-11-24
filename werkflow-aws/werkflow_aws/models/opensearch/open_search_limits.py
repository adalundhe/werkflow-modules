from __future__ import annotations
from pydantic import BaseModel
from .open_search_additional_limit import OpenSearchAdditionalLimit
from .open_search_instance_limits import OpenSearchInstanceLimits
from .open_search_storage_type import OpenSearchStorageType


class OpenSearchLimits(BaseModel):
    StorageTypes: list[OpenSearchStorageType] | None = None
    InstanceLimits: OpenSearchInstanceLimits | None = None
    AdditionalLimits: list[OpenSearchAdditionalLimit] | None = None
