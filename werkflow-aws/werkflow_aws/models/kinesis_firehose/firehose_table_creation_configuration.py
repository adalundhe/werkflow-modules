from __future__ import annotations
from pydantic import BaseModel, StrictBool


class FirehoseTableCreationConfiguration(BaseModel):
    Enabled: StrictBool | None = None
