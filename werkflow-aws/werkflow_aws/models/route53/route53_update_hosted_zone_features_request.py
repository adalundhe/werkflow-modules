from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .route53_change_guardrail_model import Route53ChangeGuardrailModel


class Route53UpdateHostedZoneFeaturesRequest(BaseModel):
    HostedZoneId: StrictStr
    EnableAcceleratedRecovery: StrictBool | None = None
    EnablePublicDNSFallback: StrictBool | None = None
    ChangeGuardrails: list[Route53ChangeGuardrailModel] | None = None
    DryRun: StrictBool | None = None
