from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AmplifySubDomainSetting(BaseModel):
    prefix: StrictStr | None = None
    branchName: StrictStr | None = None
