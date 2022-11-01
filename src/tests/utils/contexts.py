# utils/contexts.py
from aws_lambda_typing.context import Client, ClientContext, Context, Identity


class TestContext(Context):
    def __init__(self) -> None:
        super().__init__()
        self.function_name = "FUNCTION_NAME"
        self.function_version = "FUNCTION_VERSION"
        self.invoked_function_arn = "INVOKED_FUNCTION_ARN"
        self.memory_limit_in_mb = "MEMORY_LIMIT_IN_MB"
        self.aws_request_id = "AWS_REQUEST_ID"
        self.log_group_name = "LOG_GROUP_NAME"
        self.log_stream_name = "LOG_STREAM_NAME"
        self.identity = Identity(
            cognito_identity_id="COGNITO_IDENTITY_ID",
            cognito_identity_pool_id="COGNITO_IDENTITY_POOL_ID",
        )
        self.client_context = ClientContext(
            client=Client(
                app_package_name="APP_PACKAGE_NAME",
                app_title="APP_TITLE",
                app_version_code="APP_VERSION_CODE",
                app_version_name="APP_VERSION_NAME",
                installation_id="INSTALLATION_ID",
            ),
            custom={"key": "val"},
            env={"key": "val"},
        )


TEST_CONTEXT = TestContext()
