from __future__ import annotations
from pydantic import BaseModel
from .open_search_ai_config import OpenSearchAIConfig


class OpenSearchCapabilityBaseRequestConfig(BaseModel):
    aiConfig: OpenSearchAIConfig | None = None
