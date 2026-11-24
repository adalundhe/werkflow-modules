from __future__ import annotations
from pydantic import BaseModel
from .el_bv2_query_string_key_value_pair import ELBv2QueryStringKeyValuePair


class ELBv2QueryStringConditionConfig(BaseModel):
    Values: list[ELBv2QueryStringKeyValuePair] | None = None
