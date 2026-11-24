from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyVpcEncryptionControlRequest(BaseModel):
    VpcEncryptionControlId: StrictStr
    DryRun: StrictBool | None = None
    Mode: Literal['monitor', 'enforce'] | None = None
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
