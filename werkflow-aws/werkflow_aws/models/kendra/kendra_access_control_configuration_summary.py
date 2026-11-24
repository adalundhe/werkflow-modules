from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraAccessControlConfigurationSummary(BaseModel):
    Id: StrictStr | None = None
