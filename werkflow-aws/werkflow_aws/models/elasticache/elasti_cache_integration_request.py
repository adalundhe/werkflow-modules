from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class ElastiCacheIntegrationRequest(BaseModel):
    IntegrationType: Literal['dynamodb'] | None = None
