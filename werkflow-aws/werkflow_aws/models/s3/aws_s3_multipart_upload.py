from pydantic import BaseModel, conlist
from typing import List
from .aws_s3_multipart_upload_part import AWSs3MultipartUploadPart

class AWSs3MultipartUpload(BaseModel):
    parts: conlist(
        AWSs3MultipartUploadPart,
        min_length=1
    )

    def to_options(self):
        parts: List[AWSs3MultipartUploadPart] = self.parts
        return {
            'parts': [
                partto_data() for part in parts
            ]
        }