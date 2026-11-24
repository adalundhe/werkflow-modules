from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightPolicyPrincipal(BaseModel):
    PrincipalArn: StrictStr | None = None
    PrincipalType: StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    Revision: StrictInt | None = None
