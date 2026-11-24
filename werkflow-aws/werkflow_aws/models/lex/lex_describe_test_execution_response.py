from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_test_execution_target import LexTestExecutionTarget


class LexDescribeTestExecutionResponse(BaseModel):
    testExecutionId: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    testExecutionStatus: StrictStr | None = None
    testSetId: StrictStr | None = None
    testSetName: StrictStr | None = None
    target: LexTestExecutionTarget | None = None
    apiMode: StrictStr | None = None
    testExecutionModality: StrictStr | None = None
    failureReasons: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
