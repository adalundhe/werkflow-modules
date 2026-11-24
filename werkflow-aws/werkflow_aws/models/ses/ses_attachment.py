from __future__ import annotations
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class SESAttachment(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    RawContent: StrictBytes | BinaryIO | StrictStr
    FileName: StrictStr
    ContentDisposition: Literal['ATTACHMENT', 'INLINE'] | None = None
    ContentDescription: StrictStr | None = None
    ContentId: StrictStr | None = None
    ContentTransferEncoding: Literal['BASE64', 'QUOTED_PRINTABLE', 'SEVEN_BIT'] | None = None
    ContentType: StrictStr | None = None
