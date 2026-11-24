from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool


class EC2ModifyAccountVpcEncryptionControlRequest(BaseModel):
    DryRun: StrictBool | None = None
    Mode: Literal['unmanaged', 'attempt-monitor', 'attempt-enforce'] | None = None
    InternetGateway: Literal['enable', 'disable'] | None = None
    EgressOnlyInternetGateway: Literal['enable', 'disable'] | None = None
    NatGateway: Literal['enable', 'disable'] | None = None
    VirtualPrivateGateway: Literal['enable', 'disable'] | None = None
    VpcPeering: Literal['enable', 'disable'] | None = None
    Lambda: Literal['enable', 'disable'] | None = None
    VpcLattice: Literal['enable', 'disable'] | None = None
    ElasticFileSystem: Literal['enable', 'disable'] | None = None
    GlobalAccelerator: Literal['enable', 'disable'] | None = None
    ApiGatewayV2: Literal['enable', 'disable'] | None = None
