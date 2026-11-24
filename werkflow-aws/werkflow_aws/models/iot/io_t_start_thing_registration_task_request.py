from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTStartThingRegistrationTaskRequest(BaseModel):
    templateBody: StrictStr
    inputFileBucket: StrictStr
    inputFileKey: StrictStr
    roleArn: StrictStr
