from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISUpdateTargetAccountConfigurationRequest(BaseModel):
    experimentTemplateId: StrictStr
    accountId: StrictStr
    roleArn: StrictStr | None = None
    description: StrictStr | None = None
