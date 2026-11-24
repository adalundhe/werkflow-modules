from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ELBv2ClientCertificateIdentityFilter(BaseModel):
    Field: StrictStr | None = None
    Action: StrictStr | None = None
    MatchType: StrictStr | None = None
    Value: StrictStr | None = None
