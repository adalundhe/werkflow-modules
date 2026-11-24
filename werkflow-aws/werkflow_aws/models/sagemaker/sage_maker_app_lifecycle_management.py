from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_idle_settings import SageMakerIdleSettings


class SageMakerAppLifecycleManagement(BaseModel):
    IdleSettings: SageMakerIdleSettings | None = None
