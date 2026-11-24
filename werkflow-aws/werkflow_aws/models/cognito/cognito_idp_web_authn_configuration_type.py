from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPWebAuthnConfigurationType(BaseModel):
    RelyingPartyId: StrictStr | None = None
    UserVerification: StrictStr | None = None
    FactorConfiguration: StrictStr | None = None
