from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISCreateTargetAccountConfigurationRequest(BaseModel):
    experimentTemplateId: StrictStr
    accountId: StrictStr
    roleArn: StrictStr
    clientToken: StrictStr | None = None
    description: StrictStr | None = None
