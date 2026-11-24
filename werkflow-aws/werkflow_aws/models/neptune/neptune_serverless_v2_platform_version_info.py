from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .neptune_serverless_v2_features_support import NeptuneServerlessV2FeaturesSupport


class NeptuneServerlessV2PlatformVersionInfo(BaseModel):
    ServerlessV2PlatformVersion: StrictStr | None = None
    ServerlessV2PlatformVersionDescription: StrictStr | None = None
    Engine: StrictStr | None = None
    ServerlessV2FeaturesSupport: NeptuneServerlessV2FeaturesSupport | None = None
    Status: StrictStr | None = None
    IsDefault: StrictBool | None = None
