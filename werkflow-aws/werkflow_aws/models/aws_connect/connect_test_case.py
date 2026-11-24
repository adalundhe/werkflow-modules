from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .connect_test_case_entry_point import ConnectTestCaseEntryPoint


class ConnectTestCase(BaseModel):
    Arn: StrictStr | None = None
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Content: StrictStr | None = None
    EntryPoint: ConnectTestCaseEntryPoint | None = None
    InitializationData: StrictStr | None = None
    Description: StrictStr | None = None
    Status: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    TestCaseSha256: StrictStr | None = None
