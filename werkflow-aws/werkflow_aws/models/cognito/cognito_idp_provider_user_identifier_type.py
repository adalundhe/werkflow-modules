from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPProviderUserIdentifierType(BaseModel):
    ProviderName: StrictStr | None = None
    ProviderAttributeName: StrictStr | None = None
    ProviderAttributeValue: StrictStr | None = None
