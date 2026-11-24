from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class GluePutAttachmentResponse(BaseModel):
    AssetId: StrictStr | None = None
    IterableFormName: StrictStr | None = None
    ItemId: StrictStr | None = None
    AttachmentName: StrictStr | None = None
    FormTypeId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
