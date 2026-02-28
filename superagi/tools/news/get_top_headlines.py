from typing import Optional, Type
from pydantic import BaseModel, Field
from superagi.tools.base_tool import BaseTool
import requests


class GetTopHeadlinesInput(BaseModel):
    country: str = Field(..., description="The 2-letter ISO 3166-1 code of the country you want to get headlines for. e.g., 'us', 'gb', 'cn'")
    category: Optional[str] = Field(None, description="The category you want to get headlines for. Possible options: business, entertainment, general, health, science, sports, technology")
    page_size: Optional[int] = Field(10, description="Number of results to return per page. Default 10, maximum 100.")


class GetTopHeadlinesTool(BaseTool):
    name: str = "Get Top Headlines"
    args_schema: Type[BaseModel] = GetTopHeadlinesInput
    description: str = "Retrieve top headlines from NewsAPI for a specific country and category"

    def _execute(self, country: str, category: Optional[str] = None, page_size: Optional[int] = 10):
        """
        Retrieve top headlines from NewsAPI.
        
        Args:
            country: The 2-letter ISO 3166-1 code of the country
            category: The category to filter by (optional)
            page_size: Number of results to return (default 10)
        
        Returns:
            A list of top headlines with title, description, source, and URL
        """
        api_key = self.get_tool_config("NEWS_API_KEY")
        if not api_key:
            return "Error: NEWS_API_KEY is not configured."
        
        base_url = "https://newsapi.org/v2/top-headlines"
        params = {
            "country": country,
            "apiKey": api_key,
            "pageSize": page_size
        }
        
        if category:
            params["category"] = category
        
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            if data.get("status") != "ok":
                return f"Error: {data.get('message', 'Unknown error')}"
            
            articles = data.get("articles", [])
            if not articles:
                return "No headlines found for the specified parameters."
            
            result = "Top Headlines:\n\n"
            for i, article in enumerate(articles, 1):
                title = article.get("title", "No title")
                source = article.get("source", {}).get("name", "Unknown source")
                description = article.get("description", "No description")
                url = article.get("url", "")
                
                result += f"{i}. **{title}**\n"
                result += f"   Source: {source}\n"
                result += f"   {description}\n"
                result += f"   URL: {url}\n\n"
            
            return result
            
        except requests.exceptions.RequestException as e:
            return f"Error fetching headlines: {str(e)}"