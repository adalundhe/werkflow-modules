from __future__ import annotations
from pydantic import BaseModel
from .route53_resource_tag_set import Route53ResourceTagSet


class Route53ListTagsForResourceResponse(BaseModel):
    ResourceTagSet: Route53ResourceTagSet | None = None
