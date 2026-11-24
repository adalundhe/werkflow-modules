from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecr_image_identifier import ECRImageIdentifier


class ECRUpdateImageStorageClassResponse(BaseModel):
    registryId: StrictStr | None = None
    repositoryName: StrictStr | None = None
    imageId: ECRImageIdentifier | None = None
    imageStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
