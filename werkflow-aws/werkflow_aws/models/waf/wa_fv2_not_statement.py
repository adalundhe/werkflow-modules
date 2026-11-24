from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel

if TYPE_CHECKING:
    from .wa_fv2_statement import WAFv2Statement


class WAFv2NotStatement(BaseModel):
    Statement: WAFv2Statement | None = None
