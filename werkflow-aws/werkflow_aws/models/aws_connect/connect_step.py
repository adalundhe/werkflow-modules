from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_expiry import ConnectExpiry
from .connect_expression import ConnectExpression


class ConnectStep(BaseModel):
    Expiry: ConnectExpiry | None = None
    Expression: ConnectExpression | None = None
    Status: StrictStr | None = None
