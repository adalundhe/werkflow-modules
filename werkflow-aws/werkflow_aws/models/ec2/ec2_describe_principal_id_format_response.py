from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_principal_id_format import EC2PrincipalIdFormat


class EC2DescribePrincipalIdFormatResponse(BaseModel):
    Principals: list[EC2PrincipalIdFormat] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
