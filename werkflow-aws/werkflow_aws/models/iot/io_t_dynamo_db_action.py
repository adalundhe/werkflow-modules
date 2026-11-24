from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDynamoDBAction(BaseModel):
    tableName: StrictStr | None = None
    roleArn: StrictStr | None = None
    operation: StrictStr | None = None
    hashKeyField: StrictStr | None = None
    hashKeyValue: StrictStr | None = None
    hashKeyType: StrictStr | None = None
    rangeKeyField: StrictStr | None = None
    rangeKeyValue: StrictStr | None = None
    rangeKeyType: StrictStr | None = None
    payloadField: StrictStr | None = None
