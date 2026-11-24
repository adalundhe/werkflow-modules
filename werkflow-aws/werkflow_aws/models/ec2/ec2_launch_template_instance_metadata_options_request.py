from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt


class EC2LaunchTemplateInstanceMetadataOptionsRequest(BaseModel):
    HttpTokens: Literal['optional', 'required'] | None = None
    HttpPutResponseHopLimit: StrictInt | None = None
    HttpEndpoint: Literal['disabled', 'enabled'] | None = None
    HttpProtocolIpv6: Literal['disabled', 'enabled'] | None = None
    InstanceMetadataTags: Literal['disabled', 'enabled'] | None = None
