from typing import Type
from pydantic import BaseModel, Field
from superagi.tools.base_tool import BaseTool
import json


class UpdateRecordInput(BaseModel):
    object_name: str = Field(..., description="The Salesforce object name")
    record_id: str = Field(..., description="The ID of the record to update")
    update_data: str = Field(..., description="JSON string containing the fields to update")


class UpdateRecordTool(BaseTool):
    name: str = "Update Salesforce Record"
    args_schema: Type[BaseModel] = UpdateRecordInput
    description: str = "Update an existing record in Salesforce"

    def _execute(self, object_name: str, record_id: str, update_data: str):
        """
        Update a record in Salesforce.
        
        Args:
            object_name: The Salesforce object name
            record_id: The record ID
            update_data: JSON string with fields to update
        
        Returns:
            Success or error message
        """
        try:
            data = json.loads(update_data)
        except json.JSONDecodeError:
            return "Error: update_data must be a valid JSON string"
        
        return f"Update {object_name} Record {record_id}:\n{json.dumps(data, indent=2)}\n\nNote: Configure Salesforce credentials to execute. This tool requires simple-salesforce library and valid API credentials."