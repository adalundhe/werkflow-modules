from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_data_share import RedshiftDataShare


class RedshiftDescribeDataSharesForConsumerResponse(BaseModel):
    DataShares: list[RedshiftDataShare] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
