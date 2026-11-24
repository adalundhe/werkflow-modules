from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .redshift_authentication_profile import RedshiftAuthenticationProfile


class RedshiftDescribeAuthenticationProfilesResponse(BaseModel):
    AuthenticationProfiles: list[RedshiftAuthenticationProfile] | None = None
    ResponseMetadata: dict[str, Any] | None = None
