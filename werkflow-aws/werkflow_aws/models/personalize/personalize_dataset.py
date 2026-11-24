from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .personalize_dataset_update_summary import PersonalizeDatasetUpdateSummary


class PersonalizeDataset(BaseModel):
    name: StrictStr | None = None
    datasetArn: StrictStr | None = None
    datasetGroupArn: StrictStr | None = None
    datasetType: StrictStr | None = None
    schemaArn: StrictStr | None = None
    status: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    latestDatasetUpdate: PersonalizeDatasetUpdateSummary | None = None
    trackingId: StrictStr | None = None
