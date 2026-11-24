from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineActionTypeUrls(BaseModel):
    configurationUrl: StrictStr | None = None
    entityUrlTemplate: StrictStr | None = None
    executionUrlTemplate: StrictStr | None = None
    revisionUrlTemplate: StrictStr | None = None
