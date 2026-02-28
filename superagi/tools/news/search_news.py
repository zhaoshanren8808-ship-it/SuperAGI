from typing import Optional, Type
from pydantic import BaseModel, Field
from superagi.tools.base_tool import BaseTool
import requests


class SearchNewsInput(BaseModel):
    query: str = Field(..., description="The search query to find news articles")
    language: Optional[str] = Field("en", description="The 2-letter ISO-639-1 code of the language you want to search in. e.g., 'en', 'zh', 'es'")
    sort_by: Optional[str] = Field("publishedAt", description="The order to sort the articles in. Possible options: relevancy, popularity, publishedAt")
    page_size: Optional[int] = Field(10, description="Number of results to return per page. Default 10, maximum 100.")


class SearchNewsTool(BaseTool):
    name: str = "Search News"
    args_schema: Type[BaseModel] = SearchNewsInput
    description: str = "Search for news articles using keywords and apply various filters"

    def _execute(self, query: str, language: Optional[str] = "en", sort_by: Optional[str] = "publishedAt", page_size: Optional[int] = 10):
        """
        Search for news articles using NewsAPI.
        
        Args:
            query: The search query
            language: The language code (default 'en')
            sort_by: How to sort the results (default 'publishedAt')
            page_size: Number of results to return (default 10)
        
        Returns:
            A list of news articles matching the search query
        """
        api_key = self.get_tool_config("NEWS_API_KEY")
        if not api_key:
            return "Error: NEWS_API_KEY is not configured."
        
        base_url = "https://newsapi.org/v2/everything"
        params = {
            "q": query,
            "language": language,
            "sortBy": sort_by,
            "pageSize": page_size,
            "apiKey": api_key
        }
        
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            if data.get("status") != "ok":
                return f"Error: {data.get('message', 'Unknown error')}"
            
            articles = data.get("articles", [])
            if not articles:
                return f"No articles found for query: '{query}'"
            
            result = f"Search Results for '{query}':\n\n"
            for i, article in enumerate(articles, 1):
                title = article.get("title", "No title")
                source = article.get("source", {}).get("name", "Unknown source")
                description = article.get("description", "No description")
                published_at = article.get("publishedAt", "Unknown date")
                url = article.get("url", "")
                
                result += f"{i}. **{title}**\n"
                result += f"   Source: {source}\n"
                result += f"   Published: {published_at}\n"
                result += f"   {description}\n"
                result += f"   URL: {url}\n\n"
            
            return result
            
        except requests.exceptions.RequestException as e:
            return f"Error searching news: {str(e)}"