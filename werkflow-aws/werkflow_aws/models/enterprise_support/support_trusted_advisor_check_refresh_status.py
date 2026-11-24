from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SupportTrustedAdvisorCheckRefreshStatus(BaseModel):
    checkId: StrictStr | None = None
    status: StrictStr | None = None
    millisUntilNextRefreshable: StrictInt | None = None
