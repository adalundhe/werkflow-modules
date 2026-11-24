from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRNotebookS3LocationForOutput(BaseModel):
    Bucket: StrictStr | None = None
    Key: StrictStr | None = None
