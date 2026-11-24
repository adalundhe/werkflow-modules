from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from .user_details import UserDetails


class Attachment(BaseModel):
    model_config = ConfigDict(extra="allow")

    author: UserDetails | None = None
    content: StrictStr | None = None
    created: StrictStr | None = None
    filename: StrictStr | None = None
    id: StrictStr | None = None
    mimeType: StrictStr | None = None
    self: StrictStr | None = None
    size: StrictInt | None = None
    thumbnail: StrictStr | None = None
