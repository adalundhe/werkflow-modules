from __future__ import annotations
from pydantic import BaseModel, StrictBool


class FirehoseSchemaEvolutionConfiguration(BaseModel):
    Enabled: StrictBool | None = None
