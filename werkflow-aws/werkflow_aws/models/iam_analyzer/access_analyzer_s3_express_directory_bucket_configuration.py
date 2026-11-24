from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .access_analyzer_s3_express_directory_access_point_configuration import AccessAnalyzerS3ExpressDirectoryAccessPointConfiguration


class AccessAnalyzerS3ExpressDirectoryBucketConfiguration(BaseModel):
    bucketPolicy: StrictStr | None = None
    accessPoints: dict[StrictStr, AccessAnalyzerS3ExpressDirectoryAccessPointConfiguration] | None = None
