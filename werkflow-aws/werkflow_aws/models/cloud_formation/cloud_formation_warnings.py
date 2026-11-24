from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationWarnings(BaseModel):
    UnrecognizedResourceTypes: list[StrictStr] | None = None
