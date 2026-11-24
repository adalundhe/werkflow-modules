from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .redshift_qev2_idc_application import RedshiftQev2IdcApplication


class RedshiftModifyQev2IdcApplicationResponse(BaseModel):
    Qev2IdcApplication: RedshiftQev2IdcApplication | None = None
    ResponseMetadata: dict[str, Any] | None = None
