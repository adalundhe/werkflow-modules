from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2VpcEncryptionNonCompliantResource(BaseModel):
    Id: StrictStr | None = None
    Type: StrictStr | None = None
    Description: StrictStr | None = None
    IsExcludable: StrictBool | None = None
