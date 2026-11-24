from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .support_trusted_advisor_category_specific_summary import SupportTrustedAdvisorCategorySpecificSummary
from .support_trusted_advisor_resources_summary import SupportTrustedAdvisorResourcesSummary


class SupportTrustedAdvisorCheckSummary(BaseModel):
    checkId: StrictStr | None = None
    timestamp: StrictStr | None = None
    status: StrictStr | None = None
    hasFlaggedResources: StrictBool | None = None
    resourcesSummary: SupportTrustedAdvisorResourcesSummary | None = None
    categorySpecificSummary: SupportTrustedAdvisorCategorySpecificSummary | None = None
