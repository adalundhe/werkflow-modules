from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class SecurityHubAwsCodeBuildProjectSource(BaseModel):
    Type: StrictStr | None = None
    Location: StrictStr | None = None
    GitCloneDepth: StrictInt | None = None
    InsecureSsl: StrictBool | None = None
