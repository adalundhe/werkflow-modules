from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_f_sx_lustre_config import SageMakerFSxLustreConfig


class SageMakerEnvironmentConfig(BaseModel):
    FSxLustreConfig: SageMakerFSxLustreConfig | None = None
