from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TimestreamQuerySnsConfiguration(BaseModel):
    TopicArn: StrictStr | None = None
