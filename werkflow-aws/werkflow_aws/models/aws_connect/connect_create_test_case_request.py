from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr
from .connect_test_case_entry_point import ConnectTestCaseEntryPoint


class ConnectCreateTestCaseRequest(BaseModel):
    InstanceId: StrictStr
    Name: StrictStr
    Content: StrictStr
    Description: StrictStr | None = None
    EntryPoint: ConnectTestCaseEntryPoint | None = None
    InitializationData: StrictStr | None = None
    Status: Literal['PUBLISHED', 'SAVED'] | None = None
    TestCaseId: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
