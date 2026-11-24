from __future__ import annotations
from pydantic import BaseModel
from .fms_protocols_list_data import FMSProtocolsListData
from .fms_tag import FMSTag


class FMSPutProtocolsListRequest(BaseModel):
    ProtocolsList: FMSProtocolsListData
    TagList: list[FMSTag] | None = None
