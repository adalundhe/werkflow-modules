from __future__ import annotations
from pydantic import BaseModel, StrictBool


class BatchManagedInstancesLocalStorageConfiguration(BaseModel):
    useLocalStorage: StrictBool | None = None
