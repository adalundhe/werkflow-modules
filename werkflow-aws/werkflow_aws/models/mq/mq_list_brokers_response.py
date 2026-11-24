from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .mq_broker_summary import MQBrokerSummary


class MQListBrokersResponse(BaseModel):
    BrokerSummaries: list[MQBrokerSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
