from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_agreement_availability import BedrockAgreementAvailability


class BedrockGetFoundationModelAvailabilityResponse(BaseModel):
    modelId: StrictStr | None = None
    agreementAvailability: BedrockAgreementAvailability | None = None
    authorizationStatus: StrictStr | None = None
    entitlementAvailability: StrictStr | None = None
    regionAvailability: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
