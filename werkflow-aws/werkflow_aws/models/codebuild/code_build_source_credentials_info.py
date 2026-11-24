from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildSourceCredentialsInfo(BaseModel):
    arn: StrictStr | None = None
    serverType: StrictStr | None = None
    authType: StrictStr | None = None
    resource: StrictStr | None = None
