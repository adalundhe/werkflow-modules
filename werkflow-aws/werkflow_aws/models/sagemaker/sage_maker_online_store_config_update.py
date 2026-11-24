from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .sage_maker_ttl_duration import SageMakerTtlDuration


class SageMakerOnlineStoreConfigUpdate(BaseModel):
    TtlDuration: SageMakerTtlDuration | None = None
    StorageType: Literal['Standard', 'Standard_V2', 'InMemory'] | None = None
