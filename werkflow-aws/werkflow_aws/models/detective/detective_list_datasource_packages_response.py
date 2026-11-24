from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .detective_datasource_package_ingest_detail import DetectiveDatasourcePackageIngestDetail


class DetectiveListDatasourcePackagesResponse(BaseModel):
    DatasourcePackages: dict[StrictStr, DetectiveDatasourcePackageIngestDetail] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
