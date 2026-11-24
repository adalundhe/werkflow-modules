from __future__ import annotations
from pydantic import BaseModel
from .open_search_option_status import OpenSearchOptionStatus
from .open_search_vpc_derived_info import OpenSearchVPCDerivedInfo


class OpenSearchVPCDerivedInfoStatus(BaseModel):
    Options: OpenSearchVPCDerivedInfo | None = None
    Status: OpenSearchOptionStatus | None = None
