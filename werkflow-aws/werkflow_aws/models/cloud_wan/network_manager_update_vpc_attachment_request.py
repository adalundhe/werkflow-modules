from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_vpc_options import NetworkManagerVpcOptions


class NetworkManagerUpdateVpcAttachmentRequest(BaseModel):
    AttachmentId: StrictStr
    AddSubnetArns: list[StrictStr] | None = None
    RemoveSubnetArns: list[StrictStr] | None = None
    Options: NetworkManagerVpcOptions | None = None
