from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class BedrockAutomatedReasoningPolicySummary(BaseModel):
    policyArn: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    version: StrictStr | None = None
    policyId: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
