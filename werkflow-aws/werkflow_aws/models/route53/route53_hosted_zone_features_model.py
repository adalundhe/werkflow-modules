from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_change_guardrail_model import Route53ChangeGuardrailModel
from .route53_change_history_feature_model import Route53ChangeHistoryFeatureModel
from .route53_hosted_zone_failure_reasons_model import Route53HostedZoneFailureReasonsModel


class Route53HostedZoneFeaturesModel(BaseModel):
    AcceleratedRecoveryStatus: StrictStr | None = None
    PublicDNSFallbackStatus: StrictStr | None = None
    ChangeHistory: Route53ChangeHistoryFeatureModel | None = None
    FailureReasons: Route53HostedZoneFailureReasonsModel | None = None
    ChangeGuardrails: list[Route53ChangeGuardrailModel] | None = None
