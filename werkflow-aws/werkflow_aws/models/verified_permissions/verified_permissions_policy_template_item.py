from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsPolicyTemplateItem(BaseModel):
    policyStoreId: StrictStr | None = None
    policyTemplateId: StrictStr | None = None
    description: StrictStr | None = None
    createdDate: datetime.datetime | StrictStr | None = None
    lastUpdatedDate: datetime.datetime | StrictStr | None = None
    name: StrictStr | None = None
