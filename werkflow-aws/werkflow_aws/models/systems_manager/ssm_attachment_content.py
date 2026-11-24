from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SSMAttachmentContent(BaseModel):
    Name: StrictStr | None = None
    Size: StrictInt | None = None
    Hash: StrictStr | None = None
    HashType: StrictStr | None = None
    Url: StrictStr | None = None
