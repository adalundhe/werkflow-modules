from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class CodePipelinePipelineSummary(BaseModel):
    name: StrictStr | None = None
    version: StrictInt | None = None
    pipelineType: StrictStr | None = None
    executionMode: StrictStr | None = None
    created: datetime.datetime | StrictStr | None = None
    updated: datetime.datetime | StrictStr | None = None
