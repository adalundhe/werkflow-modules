from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .ecr_image_scan_findings_summary import ECRImageScanFindingsSummary
from .ecr_image_scan_status import ECRImageScanStatus


class ECRImageDetail(BaseModel):
    registryId: StrictStr | None = None
    repositoryName: StrictStr | None = None
    imageDigest: StrictStr | None = None
    imageTags: list[StrictStr] | None = None
    imageSizeInBytes: StrictInt | None = None
    imagePushedAt: datetime.datetime | StrictStr | None = None
    imageScanStatus: ECRImageScanStatus | None = None
    imageScanFindingsSummary: ECRImageScanFindingsSummary | None = None
    imageManifestMediaType: StrictStr | None = None
    artifactMediaType: StrictStr | None = None
    lastRecordedPullTime: datetime.datetime | StrictStr | None = None
    subjectManifestDigest: StrictStr | None = None
    imageStatus: StrictStr | None = None
    lastArchivedAt: datetime.datetime | StrictStr | None = None
    lastActivatedAt: datetime.datetime | StrictStr | None = None
