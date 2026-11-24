from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .route53_resource_tag_set_model import Route53ResourceTagSetModel


class Route53ListTagsForResourcesResponse(BaseModel):
    ResourceTagSets: list[Route53ResourceTagSetModel] | None = None
    ResponseMetadata: dict[str, Any] | None = None
