from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .connect_string_condition import ConnectStringCondition


class ConnectViewSearchCriteria(BaseModel):
    OrConditions: list[ConnectViewSearchCriteria] | None = None
    AndConditions: list[ConnectViewSearchCriteria] | None = None
    StringCondition: ConnectStringCondition | None = None
    ViewTypeCondition: Literal['CUSTOMER_MANAGED', 'AWS_MANAGED'] | None = None
    ViewStatusCondition: Literal['PUBLISHED', 'SAVED'] | None = None
