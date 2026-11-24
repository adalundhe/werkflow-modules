from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_ipam_address_history_record import EC2IpamAddressHistoryRecord


class EC2GetIpamAddressHistoryResponse(BaseModel):
    HistoryRecords: list[EC2IpamAddressHistoryRecord] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
