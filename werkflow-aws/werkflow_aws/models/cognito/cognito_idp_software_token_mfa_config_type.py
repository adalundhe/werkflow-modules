from __future__ import annotations
from pydantic import BaseModel, StrictBool


class CognitoIDPSoftwareTokenMfaConfigType(BaseModel):
    Enabled: StrictBool | None = None
