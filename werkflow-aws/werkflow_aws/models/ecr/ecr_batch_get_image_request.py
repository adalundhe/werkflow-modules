from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecr_image_identifier import ECRImageIdentifier


class ECRBatchGetImageRequest(BaseModel):
    repositoryName: StrictStr
    imageIds: list[ECRImageIdentifier]
    registryId: StrictStr | None = None
    acceptedMediaTypes: list[StrictStr] | None = None
