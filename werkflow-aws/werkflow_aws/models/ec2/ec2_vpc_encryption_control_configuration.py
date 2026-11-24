from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class EC2VpcEncryptionControlConfiguration(BaseModel):
    Mode: Literal['monitor', 'enforce']
    InternetGatewayExclusion: Literal['enable', 'disable'] | None = None
    EgressOnlyInternetGatewayExclusion: Literal['enable', 'disable'] | None = None
    NatGatewayExclusion: Literal['enable', 'disable'] | None = None
    VirtualPrivateGatewayExclusion: Literal['enable', 'disable'] | None = None
    VpcPeeringExclusion: Literal['enable', 'disable'] | None = None
    LambdaExclusion: Literal['enable', 'disable'] | None = None
    VpcLatticeExclusion: Literal['enable', 'disable'] | None = None
    ElasticFileSystemExclusion: Literal['enable', 'disable'] | None = None
    GlobalAcceleratorExclusion: Literal['enable', 'disable'] | None = None
    ApiGatewayV2Exclusion: Literal['enable', 'disable'] | None = None
