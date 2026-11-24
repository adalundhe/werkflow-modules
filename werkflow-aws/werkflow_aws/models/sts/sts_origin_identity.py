from __future__ import annotations
from pydantic import BaseModel, StrictStr


class STSOriginIdentity(BaseModel):
    Subject: StrictStr | None = None
    SubjectType: StrictStr | None = None
    Issuer: StrictStr | None = None
    FederatedProviderArn: StrictStr | None = None
