from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class HealthImagingDatastoreProperties(BaseModel):
    datastoreId: StrictStr | None = None
    datastoreName: StrictStr | None = None
    datastoreStatus: StrictStr | None = None
    kmsKeyArn: StrictStr | None = None
    lambdaAuthorizerArn: StrictStr | None = None
    losslessStorageFormat: StrictStr | None = None
    datastoreArn: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
