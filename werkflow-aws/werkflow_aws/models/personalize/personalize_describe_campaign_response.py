from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .personalize_campaign import PersonalizeCampaign


class PersonalizeDescribeCampaignResponse(BaseModel):
    campaign: PersonalizeCampaign | None = None
    ResponseMetadata: dict[str, Any] | None = None
