from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConfigServiceMemberAccountStatus(BaseModel):
    AccountId: StrictStr | None = None
    ConfigRuleName: StrictStr | None = None
    MemberAccountRuleStatus: StrictStr | None = None
    ErrorCode: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    LastUpdateTime: datetime.datetime | StrictStr | None = None
