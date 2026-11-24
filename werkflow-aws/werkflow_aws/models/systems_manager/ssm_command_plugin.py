from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class SSMCommandPlugin(BaseModel):
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    StatusDetails: StrictStr | None = None
    ResponseCode: StrictInt | None = None
    ResponseStartDateTime: datetime.datetime | StrictStr | None = None
    ResponseFinishDateTime: datetime.datetime | StrictStr | None = None
    Output: StrictStr | None = None
    StandardOutputUrl: StrictStr | None = None
    StandardErrorUrl: StrictStr | None = None
    OutputS3Region: StrictStr | None = None
    OutputS3BucketName: StrictStr | None = None
    OutputS3KeyPrefix: StrictStr | None = None
