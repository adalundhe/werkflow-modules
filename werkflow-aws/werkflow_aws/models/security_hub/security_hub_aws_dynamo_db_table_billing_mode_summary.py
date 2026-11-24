from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsDynamoDbTableBillingModeSummary(BaseModel):
    BillingMode: StrictStr | None = None
    LastUpdateToPayPerRequestDateTime: StrictStr | None = None
