from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field
from .io_t_cloudwatch_alarm_action import IoTCloudwatchAlarmAction
from .io_t_cloudwatch_logs_action import IoTCloudwatchLogsAction
from .io_t_cloudwatch_metric_action import IoTCloudwatchMetricAction
from .io_t_dynamo_db_action import IoTDynamoDBAction
from .io_t_dynamo_d_bv2_action import IoTDynamoDBv2Action
from .io_t_elasticsearch_action import IoTElasticsearchAction
from .io_t_firehose_action import IoTFirehoseAction
from .io_t_http_action import IoTHttpAction
from .io_t_influx_db_action import IoTInfluxDBAction
from .io_t_kafka_action import IoTKafkaAction
from .io_t_kinesis_action import IoTKinesisAction
from .io_t_lambda_action import IoTLambdaAction
from .io_t_location_action import IoTLocationAction
from .io_t_open_search_action import IoTOpenSearchAction
from .io_t_republish_action import IoTRepublishAction
from .io_ts3_action import IoTS3Action
from .io_t_salesforce_action import IoTSalesforceAction
from .io_t_sns_action import IoTSnsAction
from .io_t_sqs_action import IoTSqsAction
from .io_t_step_functions_action import IoTStepFunctionsAction
from .io_t_timestream_action import IoTTimestreamAction
from .iot_analytics_action import IotAnalyticsAction
from .iot_events_action import IotEventsAction
from .iot_site_wise_action import IotSiteWiseAction


class IoTAction(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    dynamoDB: IoTDynamoDBAction | None = None
    dynamoDBv2: IoTDynamoDBv2Action | None = None
    lambda_: IoTLambdaAction | None = Field(default=None, alias='lambda')
    sns: IoTSnsAction | None = None
    sqs: IoTSqsAction | None = None
    kinesis: IoTKinesisAction | None = None
    republish: IoTRepublishAction | None = None
    s3: IoTS3Action | None = None
    firehose: IoTFirehoseAction | None = None
    cloudwatchMetric: IoTCloudwatchMetricAction | None = None
    cloudwatchAlarm: IoTCloudwatchAlarmAction | None = None
    cloudwatchLogs: IoTCloudwatchLogsAction | None = None
    elasticsearch: IoTElasticsearchAction | None = None
    salesforce: IoTSalesforceAction | None = None
    iotAnalytics: IotAnalyticsAction | None = None
    iotEvents: IotEventsAction | None = None
    iotSiteWise: IotSiteWiseAction | None = None
    stepFunctions: IoTStepFunctionsAction | None = None
    timestream: IoTTimestreamAction | None = None
    http: IoTHttpAction | None = None
    kafka: IoTKafkaAction | None = None
    openSearch: IoTOpenSearchAction | None = None
    location: IoTLocationAction | None = None
    influxDB: IoTInfluxDBAction | None = None
