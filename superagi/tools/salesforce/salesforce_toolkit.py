from abc import ABC
from typing import List
from superagi.tools.base_tool import BaseTool, BaseToolkit, ToolConfiguration
from superagi.tools.salesforce.query_records import QueryRecordsTool
from superagi.tools.salesforce.create_record import CreateRecordTool
from superagi.tools.salesforce.update_record import UpdateRecordTool
from superagi.tools.salesforce.search_records import SearchRecordsTool
from superagi.types.key_type import ToolConfigKeyType


class SalesforceToolkit(BaseToolkit, ABC):
    name: str = "Salesforce Toolkit"
    description: str = "Salesforce Toolkit enables developers to interact with Salesforce's APIs for CRM operations, lead management, account management, and more."

    def get_tools(self) -> List[BaseTool]:
        return [
            QueryRecordsTool(),
            CreateRecordTool(),
            UpdateRecordTool(),
            SearchRecordsTool()
        ]

    def get_env_keys(self) -> List[ToolConfiguration]:
        return [
            ToolConfiguration(key="SALESFORCE_USERNAME", key_type=ToolConfigKeyType.STRING, is_required=True, is_secret=False),
            ToolConfiguration(key="SALESFORCE_PASSWORD", key_type=ToolConfigKeyType.STRING, is_required=True, is_secret=True),
            ToolConfiguration(key="SALESFORCE_SECURITY_TOKEN", key_type=ToolConfigKeyType.STRING, is_required=True, is_secret=True),
            ToolConfiguration(key="SALESFORCE_CONSUMER_KEY", key_type=ToolConfigKeyType.STRING, is_required=True, is_secret=True),
            ToolConfiguration(key="SALESFORCE_CONSUMER_SECRET", key_type=ToolConfigKeyType.STRING, is_required=True, is_secret=True)
        ]