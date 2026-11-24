from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .document_db_serverless_v2_features_support import DocumentDBServerlessV2FeaturesSupport


class DocumentDBServerlessV2PlatformVersionInfo(BaseModel):
    ServerlessV2PlatformVersion: StrictStr | None = None
    ServerlessV2PlatformVersionDescription: StrictStr | None = None
    Engine: StrictStr | None = None
    ServerlessV2FeaturesSupport: DocumentDBServerlessV2FeaturesSupport | None = None
    Status: StrictStr | None = None
    IsDefault: StrictBool | None = None
