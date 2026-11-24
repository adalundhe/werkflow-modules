from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AWSS3Grantee(BaseModel):
    DisplayName: StrictStr | None = None
    EmailAddress: StrictStr | None = None
    ID: StrictStr | None = None
    Type: Literal['CanonicalUser', 'AmazonCustomerByEmail', 'Group'] | None = None
    URI: StrictStr | None = None
