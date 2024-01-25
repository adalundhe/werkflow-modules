from pydantic import (
    StrictBool,
    StrictStr,
    StrictInt
)

from typing import Optional, List
from werkflow_aws.models.base import AWSBoto3Options
from werkflow_aws.models.parsing import (
    convert_key_to_boto3_arg, 
    convert_key_to_boto3_arg_upper_matching
)


class AWSs3ListPartsOptions(AWSBoto3Options):
    max_parts: Optional[StrictInt]
    part_number_marker: Optional[StrictInt]
    upload_id: Optional[StrictStr]
    expected_bucket_owner: Optional[StrictStr]
    sse_customer_algorithm: Optional[StrictStr]
    sse_customer_key: Optional[StrictStr]

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
