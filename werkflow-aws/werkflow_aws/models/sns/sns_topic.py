from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SNSTopic(BaseModel):
    TopicArn: StrictStr | None = None
