from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2IamInstanceProfile(BaseModel):
    Arn: StrictStr | None = None
    Id: StrictStr | None = None
