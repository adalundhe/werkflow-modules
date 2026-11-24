from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSClusterSetting(BaseModel):
    name: StrictStr | None = None
    value: StrictStr | None = None
