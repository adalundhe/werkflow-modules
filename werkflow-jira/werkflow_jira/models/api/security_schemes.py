from __future__ import annotations
from pydantic import BaseModel
from .security_scheme import SecurityScheme


class SecuritySchemes(BaseModel):
    issueSecuritySchemes: list[SecurityScheme] | None = None
