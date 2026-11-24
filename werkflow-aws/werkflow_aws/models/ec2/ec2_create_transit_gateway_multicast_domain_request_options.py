from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class EC2CreateTransitGatewayMulticastDomainRequestOptions(BaseModel):
    Igmpv2Support: Literal['enable', 'disable'] | None = None
    StaticSourcesSupport: Literal['enable', 'disable'] | None = None
    AutoAcceptSharedAssociations: Literal['enable', 'disable'] | None = None
