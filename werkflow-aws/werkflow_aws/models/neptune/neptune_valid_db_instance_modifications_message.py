from __future__ import annotations
from pydantic import BaseModel
from .neptune_valid_storage_options import NeptuneValidStorageOptions


class NeptuneValidDBInstanceModificationsMessage(BaseModel):
    Storage: list[NeptuneValidStorageOptions] | None = None
