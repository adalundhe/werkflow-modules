from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISGetTargetAccountConfigurationRequest(BaseModel):
    experimentTemplateId: StrictStr
    accountId: StrictStr
