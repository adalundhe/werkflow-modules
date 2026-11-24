from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineAWSSessionCredentials(BaseModel):
    accessKeyId: StrictStr | None = None
    secretAccessKey: StrictStr | None = None
    sessionToken: StrictStr | None = None
