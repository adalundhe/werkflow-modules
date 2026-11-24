from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_user_property import IoTUserProperty


class IoTMqttHeaders(BaseModel):
    payloadFormatIndicator: StrictStr | None = None
    contentType: StrictStr | None = None
    responseTopic: StrictStr | None = None
    correlationData: StrictStr | None = None
    messageExpiry: StrictStr | None = None
    userProperties: list[IoTUserProperty] | None = None
