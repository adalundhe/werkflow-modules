from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SupportTrustedAdvisorCheckDescription(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    category: StrictStr | None = None
    metadata: list[StrictStr] | None = None
