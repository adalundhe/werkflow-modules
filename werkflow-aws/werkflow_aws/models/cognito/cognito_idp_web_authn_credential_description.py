from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CognitoIDPWebAuthnCredentialDescription(BaseModel):
    CredentialId: StrictStr | None = None
    FriendlyCredentialName: StrictStr | None = None
    RelyingPartyId: StrictStr | None = None
    AuthenticatorAttachment: StrictStr | None = None
    AuthenticatorTransports: list[StrictStr] | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
