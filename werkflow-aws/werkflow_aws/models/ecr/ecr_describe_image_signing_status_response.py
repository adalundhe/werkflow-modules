from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecr_image_identifier import ECRImageIdentifier
from .ecr_image_signing_status import ECRImageSigningStatus


class ECRDescribeImageSigningStatusResponse(BaseModel):
    repositoryName: StrictStr | None = None
    imageId: ECRImageIdentifier | None = None
    registryId: StrictStr | None = None
    signingStatuses: list[ECRImageSigningStatus] | None = None
    ResponseMetadata: dict[str, Any] | None = None
