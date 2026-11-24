from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .comprehend_vpc_config import ComprehendVpcConfig


class ComprehendUpdateDataSecurityConfig(BaseModel):
    ModelKmsKeyId: StrictStr | None = None
    VolumeKmsKeyId: StrictStr | None = None
    VpcConfig: ComprehendVpcConfig | None = None
