from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_classification_result import SecurityHubClassificationResult


class SecurityHubDataClassificationDetails(BaseModel):
    DetailedResultsLocation: StrictStr | None = None
    Result: SecurityHubClassificationResult | None = None
