from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraJwtTokenTypeConfiguration(BaseModel):
    KeyLocation: StrictStr | None = None
    URL: StrictStr | None = None
    SecretManagerArn: StrictStr | None = None
    UserNameAttributeField: StrictStr | None = None
    GroupAttributeField: StrictStr | None = None
    Issuer: StrictStr | None = None
    ClaimRegex: StrictStr | None = None
