from __future__ import annotations
from pydantic import BaseModel
from .q_business_saml_configuration import QBusinessSamlConfiguration


class QBusinessWebExperienceAuthConfiguration(BaseModel):
    samlConfiguration: QBusinessSamlConfiguration | None = None
