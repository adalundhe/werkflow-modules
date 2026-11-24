from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AWSS3GranteeInput(BaseModel):
    Type: Literal['CanonicalUser', 'AmazonCustomerByEmail', 'Group']
    DisplayName: StrictStr | None = None
    EmailAddress: StrictStr | None = None
    ID: StrictStr | None = None
    URI: StrictStr | None = None
