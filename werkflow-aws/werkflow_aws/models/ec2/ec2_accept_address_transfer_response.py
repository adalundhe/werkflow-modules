from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_address_transfer import EC2AddressTransfer


class EC2AcceptAddressTransferResponse(BaseModel):
    AddressTransfer: EC2AddressTransfer | None = None
    ResponseMetadata: dict[str, Any] | None = None
