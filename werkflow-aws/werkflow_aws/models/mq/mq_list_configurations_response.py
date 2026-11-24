from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .mq_configuration import MQConfiguration


class MQListConfigurationsResponse(BaseModel):
    Configurations: list[MQConfiguration] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
