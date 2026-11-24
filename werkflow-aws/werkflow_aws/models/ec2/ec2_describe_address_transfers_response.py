from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_address_transfer import EC2AddressTransfer


class EC2DescribeAddressTransfersResponse(BaseModel):
    AddressTransfers: list[EC2AddressTransfer] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
