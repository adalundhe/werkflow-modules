from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineS3Location(BaseModel):
    bucket: StrictStr | None = None
    key: StrictStr | None = None
