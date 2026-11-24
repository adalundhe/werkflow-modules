from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_tag_resource_type import Route53TagResourceType


class Route53ListTagsForResourceRequest(BaseModel):
    ResourceType: Route53TagResourceType
    ResourceId: StrictStr
