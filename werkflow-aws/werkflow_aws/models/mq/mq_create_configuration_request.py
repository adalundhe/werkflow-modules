from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class MQCreateConfigurationRequest(BaseModel):
    EngineType: Literal['ACTIVEMQ', 'RABBITMQ']
    Name: StrictStr
    AuthenticationStrategy: Literal['SIMPLE', 'LDAP', 'CONFIG_MANAGED'] | None = None
    EngineVersion: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
