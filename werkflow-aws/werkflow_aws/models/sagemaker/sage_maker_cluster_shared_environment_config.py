from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .sage_maker_f_sx_lustre_config import SageMakerFSxLustreConfig


class SageMakerClusterSharedEnvironmentConfig(BaseModel):
    FSxLustreDeletionPolicy: Literal['DeleteIfNotUsed', 'Keep']
    FSxLustreConfig: SageMakerFSxLustreConfig
