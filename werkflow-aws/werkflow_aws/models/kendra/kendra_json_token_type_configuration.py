from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraJsonTokenTypeConfiguration(BaseModel):
    UserNameAttributeField: StrictStr | None = None
    GroupAttributeField: StrictStr | None = None
