from __future__ import annotations
from pydantic import BaseModel, StrictBool


class ECRDeleteReplication(BaseModel):
    enabled: StrictBool | None = None
