from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DynamoDBSSEDescriptionModel(BaseModel):
    Status: StrictStr | None = None
    SSEType: StrictStr | None = None
    KMSMasterKeyArn: StrictStr | None = None
    InaccessibleEncryptionDateTime: datetime.datetime | StrictStr | None = None
