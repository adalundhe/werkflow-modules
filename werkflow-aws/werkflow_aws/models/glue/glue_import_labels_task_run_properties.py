from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueImportLabelsTaskRunProperties(BaseModel):
    InputS3Path: StrictStr | None = None
    Replace: StrictBool | None = None
