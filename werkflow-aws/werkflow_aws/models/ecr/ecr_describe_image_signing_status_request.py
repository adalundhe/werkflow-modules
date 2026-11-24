from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecr_image_identifier import ECRImageIdentifier


class ECRDescribeImageSigningStatusRequest(BaseModel):
    repositoryName: StrictStr
    imageId: ECRImageIdentifier
    registryId: StrictStr | None = None
