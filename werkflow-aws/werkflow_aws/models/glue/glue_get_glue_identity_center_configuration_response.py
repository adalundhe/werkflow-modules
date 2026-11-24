from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class GlueGetGlueIdentityCenterConfigurationResponse(BaseModel):
    ApplicationArn: StrictStr | None = None
    InstanceArn: StrictStr | None = None
    Scopes: list[StrictStr] | None = None
    UserBackgroundSessionsEnabled: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
