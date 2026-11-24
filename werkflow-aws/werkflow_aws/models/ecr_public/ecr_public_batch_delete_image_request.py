from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecr_public_image_identifier import ECRPublicImageIdentifier


class ECRPublicBatchDeleteImageRequest(BaseModel):
    repositoryName: StrictStr
    imageIds: list[ECRPublicImageIdentifier]
    registryId: StrictStr | None = None
