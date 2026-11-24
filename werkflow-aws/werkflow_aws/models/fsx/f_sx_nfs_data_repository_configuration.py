from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .f_sx_auto_export_policy import FSxAutoExportPolicy


class FSxNFSDataRepositoryConfiguration(BaseModel):
    Version: StrictStr | None = None
    DnsIps: list[StrictStr] | None = None
    AutoExportPolicy: FSxAutoExportPolicy | None = None
