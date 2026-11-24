from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .personalize_campaign_summary import PersonalizeCampaignSummary


class PersonalizeListCampaignsResponse(BaseModel):
    campaigns: list[PersonalizeCampaignSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
