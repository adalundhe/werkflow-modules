from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineJobWorkerExecutorConfiguration(BaseModel):
    pollingAccounts: list[StrictStr] | None = None
    pollingServicePrincipals: list[StrictStr] | None = None
