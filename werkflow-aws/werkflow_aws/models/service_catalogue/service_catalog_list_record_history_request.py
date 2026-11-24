from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .service_catalog_access_level_filter import ServiceCatalogAccessLevelFilter
from .service_catalog_list_record_history_search_filter import ServiceCatalogListRecordHistorySearchFilter


class ServiceCatalogListRecordHistoryRequest(BaseModel):
    AcceptLanguage: StrictStr | None = None
    AccessLevelFilter: ServiceCatalogAccessLevelFilter | None = None
    SearchFilter: ServiceCatalogListRecordHistorySearchFilter | None = None
    PageSize: StrictInt | None = None
    PageToken: StrictStr | None = None
