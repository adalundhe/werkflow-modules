from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel

if TYPE_CHECKING:
    from .timestream_query_datum import TimestreamQueryDatum


class TimestreamQueryRow(BaseModel):
    Data: list[TimestreamQueryDatum] | None = None
