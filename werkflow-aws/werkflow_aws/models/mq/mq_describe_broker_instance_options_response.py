from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .mq_broker_instance_option import MQBrokerInstanceOption


class MQDescribeBrokerInstanceOptionsResponse(BaseModel):
    BrokerInstanceOptions: list[MQBrokerInstanceOption] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
