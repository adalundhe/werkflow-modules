from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecr_image_identifier import ECRImageIdentifier
from .ecr_image_scan_findings import ECRImageScanFindings
from .ecr_image_scan_status import ECRImageScanStatus


class ECRDescribeImageScanFindingsResponse(BaseModel):
    registryId: StrictStr | None = None
    repositoryName: StrictStr | None = None
    imageId: ECRImageIdentifier | None = None
    imageScanStatus: ECRImageScanStatus | None = None
    imageScanFindings: ECRImageScanFindings | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
