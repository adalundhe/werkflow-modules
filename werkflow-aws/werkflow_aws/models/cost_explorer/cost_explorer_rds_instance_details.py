from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CostExplorerRDSInstanceDetails(BaseModel):
    Family: StrictStr | None = None
    InstanceType: StrictStr | None = None
    Region: StrictStr | None = None
    DatabaseEngine: StrictStr | None = None
    DatabaseEdition: StrictStr | None = None
    DeploymentOption: StrictStr | None = None
    LicenseModel: StrictStr | None = None
    CurrentGeneration: StrictBool | None = None
    SizeFlexEligible: StrictBool | None = None
    DeploymentModel: StrictStr | None = None
