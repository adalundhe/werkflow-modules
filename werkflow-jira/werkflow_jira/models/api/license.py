from __future__ import annotations
from pydantic import BaseModel
from .licensed_application import LicensedApplication


class License(BaseModel):
    applications: list[LicensedApplication] | None = None
