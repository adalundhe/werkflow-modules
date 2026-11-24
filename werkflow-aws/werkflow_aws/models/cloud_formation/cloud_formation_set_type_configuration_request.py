from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CloudFormationSetTypeConfigurationRequest(BaseModel):
    Configuration: StrictStr
    TypeArn: StrictStr | None = None
    ConfigurationAlias: StrictStr | None = None
    TypeName: StrictStr | None = None
    Type: Literal['RESOURCE', 'MODULE', 'HOOK'] | None = None
