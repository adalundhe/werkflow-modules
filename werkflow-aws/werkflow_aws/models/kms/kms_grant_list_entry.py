from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .kms_grant_constraints import KMSGrantConstraints


class KMSGrantListEntry(BaseModel):
    KeyId: StrictStr | None = None
    GrantId: StrictStr | None = None
    Name: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    GranteePrincipal: StrictStr | None = None
    RetiringPrincipal: StrictStr | None = None
    IssuingAccount: StrictStr | None = None
    Operations: list[StrictStr] | None = None
    Constraints: KMSGrantConstraints | None = None
    GranteeServicePrincipal: StrictStr | None = None
    RetiringServicePrincipal: StrictStr | None = None
