from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class MQCreateBrokerResponse(BaseModel):
    BrokerArn: StrictStr | None = None
    BrokerId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
