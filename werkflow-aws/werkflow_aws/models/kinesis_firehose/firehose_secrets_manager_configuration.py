from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class FirehoseSecretsManagerConfiguration(BaseModel):
    SecretARN: StrictStr | None = None
    RoleARN: StrictStr | None = None
    Enabled: StrictBool | None = None
