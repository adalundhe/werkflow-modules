from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .redshift_idc_application import RedshiftIdcApplication as _RedshiftIdcApplicationType


class RedshiftModifyRedshiftIdcApplicationResponse(BaseModel):
    RedshiftIdcApplication: _RedshiftIdcApplicationType | None = None
    ResponseMetadata: dict[str, Any] | None = None
