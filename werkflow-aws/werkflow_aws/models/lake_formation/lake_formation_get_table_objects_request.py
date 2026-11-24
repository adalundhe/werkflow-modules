from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class LakeFormationGetTableObjectsRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    CatalogId: StrictStr | None = None
    TransactionId: StrictStr | None = None
    QueryAsOfTime: datetime.datetime | StrictStr | None = None
    PartitionPredicate: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
