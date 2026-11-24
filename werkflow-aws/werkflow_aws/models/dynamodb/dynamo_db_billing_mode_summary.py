from __future__ import annotations
import datetime
from pydantic import BaseModel
from .dynamo_db_billing_mode import DynamoDBBillingMode


class DynamoDBBillingModeSummary(BaseModel):
    BillingMode: DynamoDBBillingMode | None = None
    LastUpdateToPayPerRequestDateTime: datetime.datetime | None = None
