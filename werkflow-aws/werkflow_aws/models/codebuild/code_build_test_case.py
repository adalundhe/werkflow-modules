from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class CodeBuildTestCase(BaseModel):
    reportArn: StrictStr | None = None
    testRawDataPath: StrictStr | None = None
    prefix: StrictStr | None = None
    name: StrictStr | None = None
    status: StrictStr | None = None
    durationInNanoSeconds: StrictInt | None = None
    message: StrictStr | None = None
    expired: datetime.datetime | StrictStr | None = None
    testSuiteName: StrictStr | None = None
