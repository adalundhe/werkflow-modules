from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .macie_tag_value_pair import MacieTagValuePair


class MacieTagScopeTerm(BaseModel):
    comparator: StrictStr | None = None
    key: StrictStr | None = None
    tagValues: list[MacieTagValuePair] | None = None
    target: StrictStr | None = None
