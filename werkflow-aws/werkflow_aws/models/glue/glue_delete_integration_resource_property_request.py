from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDeleteIntegrationResourcePropertyRequest(BaseModel):
    ResourceArn: StrictStr
