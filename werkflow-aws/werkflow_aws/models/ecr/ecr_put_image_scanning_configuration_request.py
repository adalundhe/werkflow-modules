from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecr_image_scanning_configuration import ECRImageScanningConfiguration


class ECRPutImageScanningConfigurationRequest(BaseModel):
    repositoryName: StrictStr
    imageScanningConfiguration: ECRImageScanningConfiguration
    registryId: StrictStr | None = None
