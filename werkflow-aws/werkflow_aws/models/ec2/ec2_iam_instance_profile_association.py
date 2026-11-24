from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_iam_instance_profile import EC2IamInstanceProfile


class EC2IamInstanceProfileAssociation(BaseModel):
    AssociationId: StrictStr | None = None
    InstanceId: StrictStr | None = None
    IamInstanceProfile: EC2IamInstanceProfile | None = None
    State: StrictStr | None = None
    Timestamp: datetime.datetime | StrictStr | None = None
