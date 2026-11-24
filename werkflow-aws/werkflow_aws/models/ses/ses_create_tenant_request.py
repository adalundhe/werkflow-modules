from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ses_tag import SESTag
from .ses_tenant_suppression_attributes import SESTenantSuppressionAttributes


class SESCreateTenantRequest(BaseModel):
    TenantName: StrictStr
    Tags: list[SESTag] | None = None
    SuppressionAttributes: SESTenantSuppressionAttributes | None = None
