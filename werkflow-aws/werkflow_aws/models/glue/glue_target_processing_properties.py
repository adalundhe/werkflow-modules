from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueTargetProcessingProperties(BaseModel):
    RoleArn: StrictStr | None = None
    KmsArn: StrictStr | None = None
    ConnectionName: StrictStr | None = None
    EventBusArn: StrictStr | None = None
