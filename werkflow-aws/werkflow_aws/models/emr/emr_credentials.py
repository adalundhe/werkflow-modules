from __future__ import annotations
from pydantic import BaseModel
from .emr_username_password import EMRUsernamePassword


class EMRCredentials(BaseModel):
    UsernamePassword: EMRUsernamePassword | None = None
