from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .amount import Amount


class Metric(BaseModel):
    Amount: Amount
    Unit: StrictStr

    def model_dump(self, **kwargs: Any) -> dict[str, Any]:
        dumped = super().model_dump(**kwargs)
        if 'Amount' in dumped and dumped['Amount'] is not None:
            dumped['Amount'] = str(dumped['Amount'])
        return dumped
