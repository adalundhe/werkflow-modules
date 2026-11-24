from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CodePipelinePipelineMetadata(BaseModel):
    pipelineArn: StrictStr | None = None
    created: datetime.datetime | StrictStr | None = None
    updated: datetime.datetime | StrictStr | None = None
    pollingDisabledAt: datetime.datetime | StrictStr | None = None
