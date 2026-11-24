from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .io_t_configuration import IoTConfiguration


class IoTUpdateEventConfigurationsRequest(BaseModel):
    eventConfigurations: dict[Literal['THING', 'THING_GROUP', 'THING_TYPE', 'THING_GROUP_MEMBERSHIP', 'THING_GROUP_HIERARCHY', 'THING_TYPE_ASSOCIATION', 'JOB', 'JOB_EXECUTION', 'POLICY', 'CERTIFICATE', 'CA_CERTIFICATE'], IoTConfiguration] | None = None
