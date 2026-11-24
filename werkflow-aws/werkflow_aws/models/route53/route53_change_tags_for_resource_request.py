from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_tag import Route53Tag
from .route53_tag_resource_type import Route53TagResourceType


class Route53ChangeTagsForResourceRequest(BaseModel):
    ResourceType: Route53TagResourceType
    ResourceId: StrictStr
    AddTags: list[Route53Tag] | None = None
    RemoveTagKeys: list[StrictStr] | None = None
