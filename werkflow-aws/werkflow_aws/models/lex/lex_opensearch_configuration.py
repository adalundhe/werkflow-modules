from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .lex_exact_response_fields import LexExactResponseFields


class LexOpensearchConfiguration(BaseModel):
    domainEndpoint: StrictStr | None = None
    indexName: StrictStr | None = None
    exactResponse: StrictBool | None = None
    exactResponseFields: LexExactResponseFields | None = None
    includeFields: list[StrictStr] | None = None
