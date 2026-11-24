from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_ultra_server import SageMakerUltraServer


class SageMakerListUltraServersByReservedCapacityResponse(BaseModel):
    NextToken: StrictStr | None = None
    UltraServers: list[SageMakerUltraServer] | None = None
    ResponseMetadata: dict[str, Any] | None = None
