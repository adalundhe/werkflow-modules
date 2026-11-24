from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .cloud_search_limits import CloudSearchLimits
from .cloud_search_service_endpoint import CloudSearchServiceEndpoint


class CloudSearchDomainStatus(BaseModel):
    DomainId: StrictStr | None = None
    DomainName: StrictStr | None = None
    ARN: StrictStr | None = None
    Created: StrictBool | None = None
    Deleted: StrictBool | None = None
    DocService: CloudSearchServiceEndpoint | None = None
    SearchService: CloudSearchServiceEndpoint | None = None
    RequiresIndexDocuments: StrictBool | None = None
    Processing: StrictBool | None = None
    SearchInstanceType: StrictStr | None = None
    SearchPartitionCount: StrictInt | None = None
    SearchInstanceCount: StrictInt | None = None
    Limits: CloudSearchLimits | None = None
