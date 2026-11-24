from __future__ import annotations
from pydantic import BaseModel
from .open_search_retention_options import OpenSearchRetentionOptions


class OpenSearchClonedBlueGreenOptions(BaseModel):
    RetentionOptions: OpenSearchRetentionOptions | None = None
