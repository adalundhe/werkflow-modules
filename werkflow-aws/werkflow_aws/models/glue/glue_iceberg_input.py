from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .glue_create_iceberg_table_input import GlueCreateIcebergTableInput


class GlueIcebergInput(BaseModel):
    MetadataOperation: Literal['CREATE']
    Version: StrictStr | None = None
    CreateIcebergTableInput: GlueCreateIcebergTableInput | None = None
