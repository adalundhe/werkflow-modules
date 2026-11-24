from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightMicrosoftPurviewCredentials(BaseModel):
    SecretArn: StrictStr | None = None
