from __future__ import annotations
from pydantic import BaseModel
from .ec2_vpc_encryption_control_exclusion import EC2VpcEncryptionControlExclusion


class EC2VpcEncryptionControlExclusions(BaseModel):
    InternetGateway: EC2VpcEncryptionControlExclusion | None = None
    EgressOnlyInternetGateway: EC2VpcEncryptionControlExclusion | None = None
    NatGateway: EC2VpcEncryptionControlExclusion | None = None
    VirtualPrivateGateway: EC2VpcEncryptionControlExclusion | None = None
    VpcPeering: EC2VpcEncryptionControlExclusion | None = None
    Lambda: EC2VpcEncryptionControlExclusion | None = None
    VpcLattice: EC2VpcEncryptionControlExclusion | None = None
    ElasticFileSystem: EC2VpcEncryptionControlExclusion | None = None
    GlobalAccelerator: EC2VpcEncryptionControlExclusion | None = None
    ApiGatewayV2: EC2VpcEncryptionControlExclusion | None = None
