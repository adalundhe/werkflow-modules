from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .quick_sight_client_secret_configuration_detail import QuickSightClientSecretConfigurationDetail


class QuickSightClientSecretConfiguration(BaseModel):
    ClientSecretSourceType: Literal['IDP_PROVIDED']
    ClientSecretConfigurationDetail: QuickSightClientSecretConfigurationDetail | None = None
