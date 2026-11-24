from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class CodeCatalystGetSourceRepositoryResponse(BaseModel):
    spaceName: StrictStr | None = None
    projectName: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    lastUpdatedTime: datetime.datetime | StrictStr | None = None
    createdTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
