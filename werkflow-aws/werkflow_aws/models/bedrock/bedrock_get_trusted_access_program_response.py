from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_trusted_access_resolution_context import BedrockTrustedAccessResolutionContext


class BedrockGetTrustedAccessProgramResponse(BaseModel):
    programId: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    providerName: StrictStr | None = None
    detailsUrl: StrictStr | None = None
    enrollmentUrl: StrictStr | None = None
    status: StrictStr | None = None
    statusReason: StrictStr | None = None
    source: StrictStr | None = None
    eligibilityScope: StrictStr | None = None
    resolvedFor: BedrockTrustedAccessResolutionContext | None = None
    optIn: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
