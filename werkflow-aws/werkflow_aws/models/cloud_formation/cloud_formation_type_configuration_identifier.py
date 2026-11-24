from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationTypeConfigurationIdentifier(BaseModel):
    TypeArn: StrictStr | None = None
    TypeConfigurationAlias: StrictStr | None = None
    TypeConfigurationArn: StrictStr | None = None
    Type: StrictStr | None = None
    TypeName: StrictStr | None = None
