from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IoTSqsAction(BaseModel):
    roleArn: StrictStr | None = None
    queueUrl: StrictStr | None = None
    useBase64: StrictBool | None = None
