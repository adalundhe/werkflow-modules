from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_bundle_task_error import EC2BundleTaskError
from .ec2_storage import EC2Storage


class EC2BundleTask(BaseModel):
    InstanceId: StrictStr | None = None
    BundleId: StrictStr | None = None
    State: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    UpdateTime: datetime.datetime | StrictStr | None = None
    Storage: EC2Storage | None = None
    Progress: StrictStr | None = None
    BundleTaskError: EC2BundleTaskError | None = None
