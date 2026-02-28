# YouTube Toolkit

A toolkit for interacting with YouTube's API for video search and information retrieval.

## Features

- **Video Search**: Search for videos using keywords
- **Video Info**: Get detailed information about a video
- **Channel Info**: Get information about a YouTube channel
- **Video Comments**: Retrieve comments from a video

## Configuration

Required environment variables:
- `YOUTUBE_API_KEY`: Your YouTube Data API key (get one at Google Cloud Console)

## Tools

### VideoSearchTool
Search for YouTube videos.

**Parameters**:
- `query`: Search query
- `max_results`: Maximum results (default 10)

### VideoInfoTool
Get detailed video information.

**Parameters**:
- `video_id`: YouTube video ID

### ChannelInfoTool
Get channel information.

**Parameters**:
- `channel_id`: YouTube channel ID

### VideoCommentsTool
Get video comments.

**Parameters**:
- `video_id`: YouTube video ID
- `max_results`: Maximum comments (default 20)

## Example Usage

```
Search for Python tutorials:
query: "python tutorial"
max_results: 5

Get video info:
video_id: "dQw4w9WgXcQ"

Get channel info:
channel_id: "UCxxxxxx"
```