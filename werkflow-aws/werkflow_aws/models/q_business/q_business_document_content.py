from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr
from .q_business_s3 import QBusinessS3


class QBusinessDocumentContent(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    blob: StrictBytes | BinaryIO | StrictStr | None = None
    s3: QBusinessS3 | None = None
