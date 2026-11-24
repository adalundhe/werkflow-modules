from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DynamoDBBillingModeSummaryModel(BaseModel):
    BillingMode: StrictStr | None = None
    LastUpdateToPayPerRequestDateTime: datetime.datetime | StrictStr | None = None
