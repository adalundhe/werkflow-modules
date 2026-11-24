from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ecr_image_identifier import ECRImageIdentifier
from .ecr_lifecycle_policy_preview_filter import ECRLifecyclePolicyPreviewFilter


class ECRGetLifecyclePolicyPreviewRequest(BaseModel):
    repositoryName: StrictStr
    registryId: StrictStr | None = None
    imageIds: list[ECRImageIdentifier] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    filter: ECRLifecyclePolicyPreviewFilter | None = None
