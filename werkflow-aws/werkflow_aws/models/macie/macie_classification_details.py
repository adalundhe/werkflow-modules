from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .macie_classification_result import MacieClassificationResult


class MacieClassificationDetails(BaseModel):
    detailedResultsLocation: StrictStr | None = None
    jobArn: StrictStr | None = None
    jobId: StrictStr | None = None
    originType: StrictStr | None = None
    result: MacieClassificationResult | None = None
