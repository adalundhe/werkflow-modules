from __future__ import annotations
from pydantic import BaseModel
from .kendra_basic_authentication_configuration import KendraBasicAuthenticationConfiguration


class KendraAuthenticationConfiguration(BaseModel):
    BasicAuthentication: list[KendraBasicAuthenticationConfiguration] | None = None
