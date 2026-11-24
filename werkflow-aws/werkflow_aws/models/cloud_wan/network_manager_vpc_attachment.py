from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_attachment import NetworkManagerAttachment
from .network_manager_vpc_options import NetworkManagerVpcOptions


class NetworkManagerVpcAttachment(BaseModel):
    Attachment: NetworkManagerAttachment | None = None
    SubnetArns: list[StrictStr] | None = None
    Options: NetworkManagerVpcOptions | None = None
