from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessAppliedAttachmentsConfiguration(BaseModel):
    attachmentsControlMode: StrictStr | None = None
