from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .io_t_mqtt_headers import IoTMqttHeaders


class IoTRepublishAction(BaseModel):
    roleArn: StrictStr | None = None
    topic: StrictStr | None = None
    qos: StrictInt | None = None
    headers: IoTMqttHeaders | None = None
