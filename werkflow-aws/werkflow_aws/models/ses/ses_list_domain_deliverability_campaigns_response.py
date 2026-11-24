from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ses_domain_deliverability_campaign import SESDomainDeliverabilityCampaign


class SESListDomainDeliverabilityCampaignsResponse(BaseModel):
    DomainDeliverabilityCampaigns: list[SESDomainDeliverabilityCampaign] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
