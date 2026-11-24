from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMAttachmentInformation(BaseModel):
    Name: StrictStr | None = None
