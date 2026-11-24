from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDevEndpointCustomLibraries(BaseModel):
    ExtraPythonLibsS3Path: StrictStr | None = None
    ExtraJarsS3Path: StrictStr | None = None
