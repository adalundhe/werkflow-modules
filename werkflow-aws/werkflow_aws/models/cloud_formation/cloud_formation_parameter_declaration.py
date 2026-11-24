from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_formation_parameter_constraints import CloudFormationParameterConstraints


class CloudFormationParameterDeclaration(BaseModel):
    ParameterKey: StrictStr | None = None
    DefaultValue: StrictStr | None = None
    ParameterType: StrictStr | None = None
    NoEcho: StrictBool | None = None
    Description: StrictStr | None = None
    ParameterConstraints: CloudFormationParameterConstraints | None = None
