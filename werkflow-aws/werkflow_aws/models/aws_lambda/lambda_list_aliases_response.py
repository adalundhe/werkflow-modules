from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_alias_configuration import LambdaAliasConfiguration


class LambdaListAliasesResponse(BaseModel):
    NextMarker: StrictStr | None = None
    Aliases: list[LambdaAliasConfiguration] | None = None
