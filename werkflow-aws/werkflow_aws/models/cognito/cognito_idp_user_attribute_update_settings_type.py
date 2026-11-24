from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPUserAttributeUpdateSettingsType(BaseModel):
    AttributesRequireVerificationBeforeUpdate: list[StrictStr] | None = None
