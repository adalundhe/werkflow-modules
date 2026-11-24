from __future__ import annotations
from pydantic import BaseModel
from .cloud_front_tag import CloudFrontTag


class CloudFrontTags(BaseModel):
    Items: list[CloudFrontTag] | None = None
