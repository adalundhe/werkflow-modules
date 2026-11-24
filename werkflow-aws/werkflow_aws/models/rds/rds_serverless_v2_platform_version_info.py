from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .rds_serverless_v2_features_support import RDSServerlessV2FeaturesSupport


class RDSServerlessV2PlatformVersionInfo(BaseModel):
    ServerlessV2PlatformVersion: StrictStr | None = None
    ServerlessV2PlatformVersionDescription: StrictStr | None = None
    Engine: StrictStr | None = None
    ServerlessV2FeaturesSupport: RDSServerlessV2FeaturesSupport | None = None
    Status: StrictStr | None = None
    IsDefault: StrictBool | None = None
