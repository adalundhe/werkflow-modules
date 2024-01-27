from pydantic import BaseModel
from werkflow_aws.models.parsing import convert_key_to_boto3_arg



class AWSBoto3Base(BaseModel):

    def _filtered_options_to_dict(self):

        options = self.model_dump()

        return {
            key: value for key, value in options.items() if value is not None
        }

    def to_data(self):
        return {
            convert_key_to_boto3_arg(
                key
            ): value for key, value in self._filtered_options_to_dict()
        }

