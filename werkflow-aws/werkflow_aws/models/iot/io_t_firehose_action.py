from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IoTFirehoseAction(BaseModel):
    roleArn: StrictStr | None = None
    deliveryStreamName: StrictStr | None = None
    separator: StrictStr | None = None
    batchMode: StrictBool | None = None
