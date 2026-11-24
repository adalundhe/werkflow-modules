from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class GlueSupportedDialect(BaseModel):
    Dialect: Literal['REDSHIFT', 'ATHENA', 'SPARK'] | None = None
    DialectVersion: StrictStr | None = None
