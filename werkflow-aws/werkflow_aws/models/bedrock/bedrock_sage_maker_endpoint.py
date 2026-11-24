from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .bedrock_vpc_config import BedrockVpcConfig


class BedrockSageMakerEndpoint(BaseModel):
    initialInstanceCount: StrictInt | None = None
    instanceType: StrictStr | None = None
    executionRole: StrictStr | None = None
    kmsEncryptionKey: StrictStr | None = None
    vpc: BedrockVpcConfig | None = None
