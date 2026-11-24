from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .dms_collector_short_info_response import DMSCollectorShortInfoResponse
from .dms_database_instance_software_details_response import DMSDatabaseInstanceSoftwareDetailsResponse
from .dms_server_short_info_response import DMSServerShortInfoResponse


class DMSDatabaseResponse(BaseModel):
    DatabaseId: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    IpAddress: StrictStr | None = None
    NumberOfSchemas: StrictInt | None = None
    Server: DMSServerShortInfoResponse | None = None
    SoftwareDetails: DMSDatabaseInstanceSoftwareDetailsResponse | None = None
    Collectors: list[DMSCollectorShortInfoResponse] | None = None
