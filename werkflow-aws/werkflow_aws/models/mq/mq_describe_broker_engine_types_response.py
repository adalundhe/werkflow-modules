from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .mq_broker_engine_type import MQBrokerEngineType


class MQDescribeBrokerEngineTypesResponse(BaseModel):
    BrokerEngineTypes: list[MQBrokerEngineType] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
