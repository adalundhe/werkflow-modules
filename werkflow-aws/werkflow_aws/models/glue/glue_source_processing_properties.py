from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueSourceProcessingProperties(BaseModel):
    RoleArn: StrictStr | None = None
