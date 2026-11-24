from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_kafka_action_header import IoTKafkaActionHeader


class IoTKafkaAction(BaseModel):
    destinationArn: StrictStr | None = None
    topic: StrictStr | None = None
    key: StrictStr | None = None
    partition: StrictStr | None = None
    clientProperties: dict[StrictStr, StrictStr] | None = None
    headers: list[IoTKafkaActionHeader] | None = None
