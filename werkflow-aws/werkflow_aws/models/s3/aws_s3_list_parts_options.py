from pydantic import (
    StrictStr,
    StrictInt
)

from typing import Optional
from werkflow_aws.models.base import AWSBoto3Base
from werkflow_aws.models.parsing import (
    convert_key_to_boto3_arg, 
    convert_key_to_boto3_arg_upper_matching
)


class AWSs3ListPartsOptions(AWSBoto3Base):
    max_parts: Optional[StrictInt]=None
    part_number_marker: Optional[StrictInt]=None
    upload_id: Optional[StrictStr]=None
    expected_bucket_owner: Optional[StrictStr]=None
    sse_customer_algorithm: Optional[StrictStr]=None
    sse_customer_key: Optional[StrictStr]=None

    def to_options(self):

        options = self._filtered_options_to_dict()

        sse_options = {
            convert_key_to_boto3_arg_upper_matching(
                key,
                ['sse']
            ): value for key, value in options.items() if key.startswith('sse')
        }

        parsed_options = {
            convert_key_to_boto3_arg(
                key
            ): value for key, value in options.items()
        }

        parsed_options.update(sse_options)

        return parsed_options
