from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerManagedConfiguration(BaseModel):
    ManagedStorageType: StrictStr | None = None
