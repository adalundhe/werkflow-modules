from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsPolicyStoreAliasItem(BaseModel):
    aliasName: StrictStr | None = None
    policyStoreId: StrictStr | None = None
    aliasArn: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    state: StrictStr | None = None
