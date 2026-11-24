from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSFargateProfileSelector(BaseModel):
    namespace: StrictStr | None = None
    labels: dict[StrictStr, StrictStr] | None = None
