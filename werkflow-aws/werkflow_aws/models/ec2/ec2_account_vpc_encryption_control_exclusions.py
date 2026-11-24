from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2AccountVpcEncryptionControlExclusions(BaseModel):
    InternetGateway: StrictStr | None = None
    EgressOnlyInternetGateway: StrictStr | None = None
    NatGateway: StrictStr | None = None
    VirtualPrivateGateway: StrictStr | None = None
    VpcPeering: StrictStr | None = None
    Lambda: StrictStr | None = None
    VpcLattice: StrictStr | None = None
    ElasticFileSystem: StrictStr | None = None
    GlobalAccelerator: StrictStr | None = None
    ApiGatewayV2: StrictStr | None = None
