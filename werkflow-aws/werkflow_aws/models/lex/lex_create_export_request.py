from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .lex_export_resource_specification import LexExportResourceSpecification


class LexCreateExportRequest(BaseModel):
    resourceSpecification: LexExportResourceSpecification
    fileFormat: Literal['LexJson', 'TSV', 'CSV']
    filePassword: StrictStr | None = None
