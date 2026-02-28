from typing import Type
from pydantic import BaseModel, Field
from superagi.tools.base_tool import BaseTool
import json


class CreateRecordInput(BaseModel):
    object_name: str = Field(..., description="The Salesforce object name (e.g., 'Account', 'Contact', 'Lead')")
    record_data: str = Field(..., description="JSON string containing the record fields and values")


class CreateRecordTool(BaseTool):
    name: str = "Create Salesforce Record"
    args_schema: Type[BaseModel] = CreateRecordInput
    description: str = "Create a new record in Salesforce"

    def _execute(self, object_name: str, record_data: str):
        """
        Create a new record in Salesforce.
        
        Args:
            object_name: The Salesforce object name
            record_data: JSON string with record fields
        
        Returns:
            The created record ID or error message
        """
        try:
            data = json.loads(record_data)
        except json.JSONDecodeError:
            return "Error: record_data must be a valid JSON string"
        
        return f"Create {object_name} Record:\n{json.dumps(data, indent=2)}\n\nNote: Configure Salesforce credentials to execute. This tool requires simple-salesforce library and valid API credentials."