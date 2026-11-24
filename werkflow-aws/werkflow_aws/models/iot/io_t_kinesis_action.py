from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTKinesisAction(BaseModel):
    roleArn: StrictStr | None = None
    streamName: StrictStr | None = None
    partitionKey: StrictStr | None = None
