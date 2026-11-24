from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubCodeVulnerabilitiesFilePath(BaseModel):
    EndLine: StrictInt | None = None
    FileName: StrictStr | None = None
    FilePath: StrictStr | None = None
    StartLine: StrictInt | None = None
