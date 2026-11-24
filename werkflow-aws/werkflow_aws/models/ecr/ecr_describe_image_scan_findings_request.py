from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ecr_image_identifier import ECRImageIdentifier


class ECRDescribeImageScanFindingsRequest(BaseModel):
    repositoryName: StrictStr
    imageId: ECRImageIdentifier
    registryId: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
