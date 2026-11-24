from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .io_t_command_parameter import IoTCommandParameter
from .io_t_command_payload import IoTCommandPayload
from .io_t_command_preprocessor import IoTCommandPreprocessor
from .io_t_tag import IoTTag


class IoTCreateCommandRequest(BaseModel):
    commandId: StrictStr
    namespace: Literal['AWS-IoT', 'AWS-IoT-FleetWise'] | None = None
    displayName: StrictStr | None = None
    description: StrictStr | None = None
    payload: IoTCommandPayload | None = None
    payloadTemplate: StrictStr | None = None
    preprocessor: IoTCommandPreprocessor | None = None
    mandatoryParameters: list[IoTCommandParameter] | None = None
    roleArn: StrictStr | None = None
    tags: list[IoTTag] | None = None
