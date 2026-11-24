from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaAllowedPublishers(BaseModel):
    SigningProfileVersionArns: list[StrictStr] | None = None
