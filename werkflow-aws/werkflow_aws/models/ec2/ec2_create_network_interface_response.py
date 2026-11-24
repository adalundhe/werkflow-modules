from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_network_interface import EC2NetworkInterface


class EC2CreateNetworkInterfaceResponse(BaseModel):
    NetworkInterface: EC2NetworkInterface | None = None
    ClientToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
