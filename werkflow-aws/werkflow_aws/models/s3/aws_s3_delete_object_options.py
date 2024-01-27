from pydantic import (
    StrictStr,
    StrictBool
)
from werkflow_aws.models.base import AWSBoto3Options
from werkflow_aws.models.parsing import (
    convert_key_to_boto3_arg,
    convert_key_to_boto3_arg_upper_matching,
    key_contains_patterns
)
from typing import Optional


class AWSs3DeleteObjectOptions(AWSBoto3Options):
    mfa: Optional[StrictStr]=None
    version_id: Optional[StrictStr]=None
    bypass_governance_retention: Optional[StrictBool]=None
    expected_bucket_owner: Optional[StrictStr]=None

    def to_options(self):

        options = self._filtered_options_to_dict()

        uppercased_options = {
            convert_key_to_boto3_arg_upper_matching(
                key,
                ['mfa']
            ): value  for key, value in options.items() if key_contains_patterns(
                key,
                ['mfa']
            )
        }

        parsed_options = {
            convert_key_to_boto3_arg(
                key
            ): value for key, value in options.items() if key not in uppercased_options
        }

        parsed_options.update(uppercased_options)

        return parsed_options