from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DynamoDBTableClassSummaryModel(BaseModel):
    TableClass: StrictStr | None = None
    LastUpdateDateTime: datetime.datetime | StrictStr | None = None
