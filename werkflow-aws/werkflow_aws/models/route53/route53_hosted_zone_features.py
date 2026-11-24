from __future__ import annotations
from pydantic import BaseModel
from .route53_accelerated_recovery_status import Route53AcceleratedRecoveryStatus
from .route53_change_guardrail import Route53ChangeGuardrail
from .route53_change_history_feature import Route53ChangeHistoryFeature
from .route53_feature_status import Route53FeatureStatus
from .route53_hosted_zone_failure_reasons import Route53HostedZoneFailureReasons


class Route53HostedZoneFeatures(BaseModel):
    AcceleratedRecoveryStatus: Route53AcceleratedRecoveryStatus | None = None
    PublicDNSFallbackStatus: Route53FeatureStatus | None = None
    ChangeHistory: Route53ChangeHistoryFeature | None = None
    FailureReasons: Route53HostedZoneFailureReasons | None = None
    ChangeGuardrails: list[Route53ChangeGuardrail] | None = None
