from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ssm_tag import SSMTag


class SSMPutParameterRequest(BaseModel):
    Name: StrictStr
    Value: StrictStr
    Description: StrictStr | None = None
    Type: Literal['String', 'StringList', 'SecureString'] | None = None
    KeyId: StrictStr | None = None
    Overwrite: StrictBool | None = None
    AllowedPattern: StrictStr | None = None
    Tags: list[SSMTag] | None = None
    Tier: Literal['Standard', 'Advanced', 'Intelligent-Tiering'] | None = None
    Policies: StrictStr | None = None
    DataType: StrictStr | None = None
