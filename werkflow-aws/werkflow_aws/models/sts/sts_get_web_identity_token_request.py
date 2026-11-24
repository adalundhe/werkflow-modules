from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .sts_tag import STSTag


class STSGetWebIdentityTokenRequest(BaseModel):
    Audience: list[StrictStr]
    SigningAlgorithm: StrictStr
    DurationSeconds: StrictInt | None = None
    Scope: StrictStr | None = None
    SubjectMode: Literal['AWSIdentity', 'OriginIdentity'] | None = None
    Tags: list[STSTag] | None = None
