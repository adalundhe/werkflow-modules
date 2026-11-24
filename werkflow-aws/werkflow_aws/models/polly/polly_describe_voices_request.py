from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class PollyDescribeVoicesRequest(BaseModel):
    Engine: Literal['standard', 'neural', 'long-form', 'generative'] | None = None
    LanguageCode: StrictStr | None = None
    IncludeAdditionalLanguageCodes: StrictBool | None = None
    NextToken: StrictStr | None = None
