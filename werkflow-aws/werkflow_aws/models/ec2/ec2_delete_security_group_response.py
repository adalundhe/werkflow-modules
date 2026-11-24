from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteSecurityGroupResponse(BaseModel):
    Return: StrictBool | None = None
    GroupId: StrictStr | None = None
