from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ses_domain_deliverability_campaign import SESDomainDeliverabilityCampaign


class SESGetDomainDeliverabilityCampaignResponse(BaseModel):
    DomainDeliverabilityCampaign: SESDomainDeliverabilityCampaign | None = None
    ResponseMetadata: dict[str, Any] | None = None
