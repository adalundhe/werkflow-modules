from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecr_image_identifier import ECRImageIdentifier


class ECRBatchDeleteImageRequest(BaseModel):
    repositoryName: StrictStr
    imageIds: list[ECRImageIdentifier]
    registryId: StrictStr | None = None
