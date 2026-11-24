from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AthenaAclConfigurationModel(BaseModel):
    S3AclOption: StrictStr | None = None
