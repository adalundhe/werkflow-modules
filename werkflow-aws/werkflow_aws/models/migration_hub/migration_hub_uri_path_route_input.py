from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class MigrationHubUriPathRouteInput(BaseModel):
    ActivationState: StrictStr | None = None
    AppendSourcePath: StrictBool | None = None
    IncludeChildPaths: StrictBool | None = None
    Methods: list[StrictStr] | None = None
    SourcePath: StrictStr | None = None
