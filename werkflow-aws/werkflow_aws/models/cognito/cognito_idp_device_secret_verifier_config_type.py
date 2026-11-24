from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPDeviceSecretVerifierConfigType(BaseModel):
    PasswordVerifier: StrictStr | None = None
    Salt: StrictStr | None = None
