from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr
from .q_business_copy_from_source import QBusinessCopyFromSource


class QBusinessAttachmentInput(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    data: StrictBytes | BinaryIO | StrictStr | None = None
    name: StrictStr | None = None
    copyFrom: QBusinessCopyFromSource | None = None
