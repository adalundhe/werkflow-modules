from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .ecr_enhanced_image_scan_finding import ECREnhancedImageScanFinding
from .ecr_image_scan_finding import ECRImageScanFinding


class ECRImageScanFindings(BaseModel):
    imageScanCompletedAt: datetime.datetime | StrictStr | None = None
    vulnerabilitySourceUpdatedAt: datetime.datetime | StrictStr | None = None
    findingSeverityCounts: dict[StrictStr, StrictInt] | None = None
    findings: list[ECRImageScanFinding] | None = None
    enhancedFindings: list[ECREnhancedImageScanFinding] | None = None
