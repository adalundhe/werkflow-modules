from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .support_trusted_advisor_category_specific_summary import SupportTrustedAdvisorCategorySpecificSummary
from .support_trusted_advisor_resource_detail import SupportTrustedAdvisorResourceDetail
from .support_trusted_advisor_resources_summary import SupportTrustedAdvisorResourcesSummary


class SupportTrustedAdvisorCheckResult(BaseModel):
    checkId: StrictStr | None = None
    timestamp: StrictStr | None = None
    status: StrictStr | None = None
    resourcesSummary: SupportTrustedAdvisorResourcesSummary | None = None
    categorySpecificSummary: SupportTrustedAdvisorCategorySpecificSummary | None = None
    flaggedResources: list[SupportTrustedAdvisorResourceDetail] | None = None
