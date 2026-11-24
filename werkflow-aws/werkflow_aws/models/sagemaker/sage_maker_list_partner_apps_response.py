from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_partner_app_summary import SageMakerPartnerAppSummary


class SageMakerListPartnerAppsResponse(BaseModel):
    Summaries: list[SageMakerPartnerAppSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
