from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ecr_describe_images_filter import ECRDescribeImagesFilter
from .ecr_image_identifier import ECRImageIdentifier


class ECRDescribeImagesRequest(BaseModel):
    repositoryName: StrictStr
    registryId: StrictStr | None = None
    imageIds: list[ECRImageIdentifier] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    filter: ECRDescribeImagesFilter | None = None
