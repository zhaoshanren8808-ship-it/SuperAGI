from typing import Type, Optional
from pydantic import BaseModel, Field
from superagi.tools.base_tool import BaseTool
import requests


class VideoSearchInput(BaseModel):
    query: str = Field(..., description="The search query to find YouTube videos")
    max_results: Optional[int] = Field(10, description="Maximum number of results to return")


class VideoSearchTool(BaseTool):
    name: str = "Search YouTube Videos"
    args_schema: Type[BaseModel] = VideoSearchInput
    description: str = "Search for videos on YouTube using keywords"

    def _execute(self, query: str, max_results: Optional[int] = 10):
        """
        Search for YouTube videos.
        
        Args:
            query: The search query
            max_results: Maximum results to return
        
        Returns:
            List of videos with title, channel, and URL
        """
        api_key = self.get_tool_config("YOUTUBE_API_KEY")
        if not api_key:
            return "Error: YOUTUBE_API_KEY is not configured."
        
        base_url = "https://www.googleapis.com/youtube/v3/search"
        params = {
            "part": "snippet",
            "q": query,
            "type": "video",
            "maxResults": max_results,
            "key": api_key
        }
        
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            items = data.get("items", [])
            if not items:
                return f"No videos found for query: '{query}'"
            
            result = f"YouTube Search Results for '{query}':\n\n"
            for i, item in enumerate(items, 1):
                video_id = item.get("id", {}).get("videoId", "")
                title = item.get("snippet", {}).get("title", "No title")
                channel = item.get("snippet", {}).get("channelTitle", "Unknown channel")
                description = item.get("snippet", {}).get("description", "")[:100]
                
                result += f"{i}. **{title}**\n"
                result += f"   Channel: {channel}\n"
                result += f"   URL: https://www.youtube.com/watch?v={video_id}\n"
                result += f"   {description}...\n\n"
            
            return result
            
        except requests.exceptions.RequestException as e:
            return f"Error searching YouTube: {str(e)}"