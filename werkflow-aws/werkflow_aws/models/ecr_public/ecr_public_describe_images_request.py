from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ecr_public_image_identifier import ECRPublicImageIdentifier


class ECRPublicDescribeImagesRequest(BaseModel):
    repositoryName: StrictStr
    registryId: StrictStr | None = None
    imageIds: list[ECRPublicImageIdentifier] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
