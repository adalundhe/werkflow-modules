from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ecr_list_images_filter import ECRListImagesFilter


class ECRListImagesRequest(BaseModel):
    repositoryName: StrictStr
    registryId: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    filter: ECRListImagesFilter | None = None
