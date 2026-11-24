from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMSessionManagerOutputUrl(BaseModel):
    S3OutputUrl: StrictStr | None = None
    CloudWatchOutputUrl: StrictStr | None = None
