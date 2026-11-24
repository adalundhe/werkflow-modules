from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr
from .connect_test_case_entry_point import ConnectTestCaseEntryPoint


class ConnectUpdateTestCaseRequest(BaseModel):
    InstanceId: StrictStr
    TestCaseId: StrictStr
    Content: StrictStr | None = None
    EntryPoint: ConnectTestCaseEntryPoint | None = None
    InitializationData: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Status: Literal['PUBLISHED', 'SAVED'] | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
