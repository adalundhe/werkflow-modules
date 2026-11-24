from __future__ import annotations
from pydantic import BaseModel
from .route53_change_guardrail_name import Route53ChangeGuardrailName
from .route53_change_guardrail_status import Route53ChangeGuardrailStatus


class Route53ChangeGuardrail(BaseModel):
    Name: Route53ChangeGuardrailName | None = None
    Status: Route53ChangeGuardrailStatus | None = None
