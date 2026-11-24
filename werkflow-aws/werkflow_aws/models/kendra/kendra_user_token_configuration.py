from __future__ import annotations
from pydantic import BaseModel
from .kendra_json_token_type_configuration import KendraJsonTokenTypeConfiguration
from .kendra_jwt_token_type_configuration import KendraJwtTokenTypeConfiguration


class KendraUserTokenConfiguration(BaseModel):
    JwtTokenTypeConfiguration: KendraJwtTokenTypeConfiguration | None = None
    JsonTokenTypeConfiguration: KendraJsonTokenTypeConfiguration | None = None
