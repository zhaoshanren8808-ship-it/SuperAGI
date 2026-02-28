from typing import Type
from pydantic import BaseModel, Field
from superagi.tools.base_tool import BaseTool


class SearchRecordsInput(BaseModel):
    search_term: str = Field(..., description="The search term to look for")
    object_names: str = Field(..., description="Comma-separated list of object names to search in (e.g., 'Account, Contact, Lead')")


class SearchRecordsTool(BaseTool):
    name: str = "Search Salesforce Records"
    args_schema: Type[BaseModel] = SearchRecordsInput
    description: str = "Search for records across multiple Salesforce objects using SOSL"

    def _execute(self, search_term: str, object_names: str):
        """
        Search records in Salesforce using SOSL.
        
        Args:
            search_term: The search term
            object_names: Comma-separated object names
        
        Returns:
            Search results
        """
        objects = [obj.strip() for obj in object_names.split(",")]
        search_query = f"FIND {{{search_term}}} IN ALL FIELDS RETURNING {', '.join(objects)}"
        
        return f"Salesforce SOSL Query: {search_query}\n\nNote: Configure Salesforce credentials to execute. This tool requires simple-salesforce library and valid API credentials."