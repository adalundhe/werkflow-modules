from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class GuardDutyAssociationDetail(BaseModel):
    AssociationId: StrictStr | None = None
    Arn: StrictStr | None = None
    RuleId: StrictStr | None = None
    AccountId: StrictStr | None = None
    Mode: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    ExpiresAt: datetime.datetime | StrictStr | None = None
