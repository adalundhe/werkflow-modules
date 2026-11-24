from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMROutputNotebookS3LocationForOutput(BaseModel):
    Bucket: StrictStr | None = None
    Key: StrictStr | None = None
