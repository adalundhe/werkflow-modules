from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .access_analyzer_network_origin_configuration import AccessAnalyzerNetworkOriginConfiguration


class AccessAnalyzerS3ExpressDirectoryAccessPointConfiguration(BaseModel):
    accessPointPolicy: StrictStr | None = None
    networkOrigin: AccessAnalyzerNetworkOriginConfiguration | None = None
