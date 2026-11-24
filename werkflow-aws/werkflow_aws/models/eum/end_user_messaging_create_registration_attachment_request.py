from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr
from .end_user_messaging_tag import EndUserMessagingTag


class EndUserMessagingCreateRegistrationAttachmentRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    AttachmentBody: StrictBytes | BinaryIO | StrictStr | None = None
    AttachmentUrl: StrictStr | None = None
    Tags: list[EndUserMessagingTag] | None = None
    ClientToken: StrictStr | None = None
