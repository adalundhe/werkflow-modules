from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSDynamoDbSettings(BaseModel):
    ServiceAccessRoleArn: StrictStr | None = None
