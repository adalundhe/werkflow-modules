from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_standards_control_association_summary import SecurityHubStandardsControlAssociationSummary


class SecurityHubListStandardsControlAssociationsResponse(BaseModel):
    StandardsControlAssociationSummaries: list[SecurityHubStandardsControlAssociationSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
