from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SupportTrustedAdvisorResourceDetail(BaseModel):
    status: StrictStr | None = None
    region: StrictStr | None = None
    resourceId: StrictStr | None = None
    isSuppressed: StrictBool | None = None
    metadata: list[StrictStr] | None = None
