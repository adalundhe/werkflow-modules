from __future__ import annotations
from pydantic import BaseModel
from .credentials import Credentials as _CredentialsModel


class GetSessionTokenResponse(BaseModel):
    Credentials: _CredentialsModel | None = None
