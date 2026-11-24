from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecr_image_scanning_configuration import ECRImageScanningConfiguration


class ECRPutImageScanningConfigurationResponse(BaseModel):
    registryId: StrictStr | None = None
    repositoryName: StrictStr | None = None
    imageScanningConfiguration: ECRImageScanningConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
