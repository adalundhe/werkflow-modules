from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_data_classification_details import SecurityHubDataClassificationDetails
from .security_hub_resource_details import SecurityHubResourceDetails
from .security_hub_resource_owner import SecurityHubResourceOwner


class SecurityHubResource(BaseModel):
    Type: StrictStr | None = None
    Id: StrictStr | None = None
    Partition: StrictStr | None = None
    Region: StrictStr | None = None
    Provider: StrictStr | None = None
    Owner: SecurityHubResourceOwner | None = None
    ResourceRole: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    DataClassification: SecurityHubDataClassificationDetails | None = None
    Details: SecurityHubResourceDetails | None = None
    ApplicationName: StrictStr | None = None
    ApplicationArn: StrictStr | None = None
