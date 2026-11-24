from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2ModifyInstanceMetadataOptionsRequest(BaseModel):
    InstanceId: StrictStr
    HttpTokens: Literal['optional', 'required'] | None = None
    HttpPutResponseHopLimit: StrictInt | None = None
    HttpEndpoint: Literal['disabled', 'enabled'] | None = None
    DryRun: StrictBool | None = None
    HttpProtocolIpv6: Literal['disabled', 'enabled'] | None = None
    InstanceMetadataTags: Literal['disabled', 'enabled'] | None = None
