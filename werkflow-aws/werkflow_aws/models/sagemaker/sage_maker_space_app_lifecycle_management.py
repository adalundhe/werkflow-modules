from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_space_idle_settings import SageMakerSpaceIdleSettings


class SageMakerSpaceAppLifecycleManagement(BaseModel):
    IdleSettings: SageMakerSpaceIdleSettings | None = None
