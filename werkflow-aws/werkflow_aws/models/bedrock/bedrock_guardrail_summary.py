from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .bedrock_guardrail_cross_region_details import BedrockGuardrailCrossRegionDetails


class BedrockGuardrailSummary(BaseModel):
    id: StrictStr | None = None
    arn: StrictStr | None = None
    status: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    version: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    crossRegionDetails: BedrockGuardrailCrossRegionDetails | None = None
