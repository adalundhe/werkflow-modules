from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .fms_protocols_list_data import FMSProtocolsListData


class FMSPutProtocolsListResponse(BaseModel):
    ProtocolsList: FMSProtocolsListData | None = None
    ProtocolsListArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
