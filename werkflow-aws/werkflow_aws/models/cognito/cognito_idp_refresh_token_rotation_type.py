from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoIDPRefreshTokenRotationType(BaseModel):
    Feature: StrictStr | None = None
    RetryGracePeriodSeconds: StrictInt | None = None
