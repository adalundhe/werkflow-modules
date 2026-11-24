from __future__ import annotations
from pydantic import BaseModel, StrictBool


class ECSManagedInstancesLocalStorageConfiguration(BaseModel):
    useLocalStorage: StrictBool | None = None
