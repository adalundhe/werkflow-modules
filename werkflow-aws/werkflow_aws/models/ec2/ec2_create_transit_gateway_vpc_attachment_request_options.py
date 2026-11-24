from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class EC2CreateTransitGatewayVpcAttachmentRequestOptions(BaseModel):
    DnsSupport: Literal['enable', 'disable'] | None = None
    SecurityGroupReferencingSupport: Literal['enable', 'disable'] | None = None
    Ipv6Support: Literal['enable', 'disable'] | None = None
    ApplianceModeSupport: Literal['enable', 'disable'] | None = None
