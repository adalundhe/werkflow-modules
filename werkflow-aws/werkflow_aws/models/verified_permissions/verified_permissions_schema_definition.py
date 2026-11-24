from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsSchemaDefinition(BaseModel):
    cedarJson: StrictStr | None = None
