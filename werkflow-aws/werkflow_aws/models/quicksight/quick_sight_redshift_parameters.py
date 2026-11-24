from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_identity_center_configuration import QuickSightIdentityCenterConfiguration
from .quick_sight_redshift_iam_parameters import QuickSightRedshiftIAMParameters


class QuickSightRedshiftParameters(BaseModel):
    Host: StrictStr | None = None
    Port: StrictInt | None = None
    Database: StrictStr | None = None
    FederatedCatalog: StrictStr | None = None
    ClusterId: StrictStr | None = None
    IAMParameters: QuickSightRedshiftIAMParameters | None = None
    IdentityCenterConfiguration: QuickSightIdentityCenterConfiguration | None = None
