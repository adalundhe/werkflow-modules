from __future__ import annotations
from pydantic import BaseModel, StrictInt


class OpenSearchServerlessSecurityConfigStats(BaseModel):
    SamlConfigCount: StrictInt | None = None
