from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_storage_type_limit import OpenSearchStorageTypeLimit


class OpenSearchStorageType(BaseModel):
    StorageTypeName: StrictStr | None = None
    StorageSubTypeName: StrictStr | None = None
    StorageTypeLimits: list[OpenSearchStorageTypeLimit] | None = None
