from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudFormationRequiredActivatedType(BaseModel):
    TypeNameAlias: StrictStr | None = None
    OriginalTypeName: StrictStr | None = None
    PublisherId: StrictStr | None = None
    SupportedMajorVersions: list[StrictInt] | None = None
