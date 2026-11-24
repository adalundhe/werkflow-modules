from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .access_analyzer_network_origin_configuration import AccessAnalyzerNetworkOriginConfiguration
from .access_analyzer_s3_public_access_block_configuration import AccessAnalyzerS3PublicAccessBlockConfiguration


class AccessAnalyzerS3AccessPointConfiguration(BaseModel):
    accessPointPolicy: StrictStr | None = None
    publicAccessBlock: AccessAnalyzerS3PublicAccessBlockConfiguration | None = None
    networkOrigin: AccessAnalyzerNetworkOriginConfiguration | None = None
