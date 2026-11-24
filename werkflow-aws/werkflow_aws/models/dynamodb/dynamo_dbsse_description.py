from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .dynamo_dbsse_status import DynamoDBSSEStatus
from .dynamo_dbsse_type import DynamoDBSSEType


class DynamoDBSSEDescription(BaseModel):
    Status: DynamoDBSSEStatus | None = None
    SSEType: DynamoDBSSEType | None = None
    KMSMasterKeyArn: StrictStr | None = None
    InaccessibleEncryptionDateTime: datetime.datetime | None = None
