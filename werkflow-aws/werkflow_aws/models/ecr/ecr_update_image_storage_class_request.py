from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .ecr_image_identifier import ECRImageIdentifier


class ECRUpdateImageStorageClassRequest(BaseModel):
    repositoryName: StrictStr
    imageId: ECRImageIdentifier
    targetStorageClass: Literal['STANDARD', 'ARCHIVE']
    registryId: StrictStr | None = None
