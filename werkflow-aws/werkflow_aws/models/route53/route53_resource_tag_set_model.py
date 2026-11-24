from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_tag_model import Route53TagModel


class Route53ResourceTagSetModel(BaseModel):
    ResourceType: StrictStr | None = None
    ResourceId: StrictStr | None = None
    Tags: list[Route53TagModel] | None = None
