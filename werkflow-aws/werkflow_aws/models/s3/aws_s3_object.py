from pydantic import StrictStr
from werkflow_aws.models.base import AWSBoto3Base


class AWSs3Object(AWSBoto3Base):
    key: StrictStr
    version_id: StrictStr | None = None
