from __future__ import annotations
from pydantic import BaseModel
from .mq_configuration_id import MQConfigurationId


class MQConfigurations(BaseModel):
    Current: MQConfigurationId | None = None
    History: list[MQConfigurationId] | None = None
    Pending: MQConfigurationId | None = None
