from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConnectCreateTestCaseResponse(BaseModel):
    TestCaseId: StrictStr | None = None
    TestCaseArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
