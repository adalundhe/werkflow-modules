from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISDeleteTargetAccountConfigurationRequest(BaseModel):
    experimentTemplateId: StrictStr
    accountId: StrictStr
