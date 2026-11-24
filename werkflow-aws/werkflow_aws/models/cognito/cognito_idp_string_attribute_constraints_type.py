from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPStringAttributeConstraintsType(BaseModel):
    MinLength: StrictStr | None = None
    MaxLength: StrictStr | None = None
