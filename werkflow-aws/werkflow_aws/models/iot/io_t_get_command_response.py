from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .io_t_command_parameter import IoTCommandParameter
from .io_t_command_payload import IoTCommandPayload
from .io_t_command_preprocessor import IoTCommandPreprocessor


class IoTGetCommandResponse(BaseModel):
    commandId: StrictStr | None = None
    commandArn: StrictStr | None = None
    namespace: StrictStr | None = None
    displayName: StrictStr | None = None
    description: StrictStr | None = None
    mandatoryParameters: list[IoTCommandParameter] | None = None
    payload: IoTCommandPayload | None = None
    payloadTemplate: StrictStr | None = None
    preprocessor: IoTCommandPreprocessor | None = None
    roleArn: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    deprecated: StrictBool | None = None
    pendingDeletion: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
