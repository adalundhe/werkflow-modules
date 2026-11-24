from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESEmailTemplateContent(BaseModel):
    Subject: StrictStr | None = None
    Text: StrictStr | None = None
    Html: StrictStr | None = None
