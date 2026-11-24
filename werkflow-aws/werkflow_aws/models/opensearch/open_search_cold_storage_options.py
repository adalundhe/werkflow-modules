from __future__ import annotations
from pydantic import BaseModel, StrictBool


class OpenSearchColdStorageOptions(BaseModel):
    Enabled: StrictBool | None = None
