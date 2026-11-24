from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .media_store_cors_rule import MediaStoreCorsRule


class MediaStorePutCorsPolicyRequest(BaseModel):
    ContainerName: StrictStr
    CorsPolicy: list[MediaStoreCorsRule]
