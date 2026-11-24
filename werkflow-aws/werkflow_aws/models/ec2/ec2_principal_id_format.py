from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_id_format import EC2IdFormat


class EC2PrincipalIdFormat(BaseModel):
    Arn: StrictStr | None = None
    Statuses: list[EC2IdFormat] | None = None
