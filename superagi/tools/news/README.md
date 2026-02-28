# News Toolkit

A toolkit for interacting with NewsAPI to retrieve and search news articles.

## Features

- **Get Top Headlines**: Retrieve top headlines from a specific country and category
- **Search News**: Search for news articles using keywords and filters

## Configuration

Required environment variables:
- `NEWS_API_KEY`: Your NewsAPI key (get one at https://newsapi.org)

## Tools

### GetTopHeadlinesTool
Retrieve top headlines from NewsAPI.

**Parameters**:
- `country`: The 2-letter ISO 3166-1 code (e.g., 'us', 'gb', 'cn')
- `category`: Optional category (business, entertainment, general, health, science, sports, technology)
- `page_size`: Number of results (default 10, max 100)

### SearchNewsTool
Search for news articles using keywords.

**Parameters**:
- `query`: The search query
- `language`: Language code (default 'en')
- `sort_by`: Sort order (relevancy, popularity, publishedAt)
- `page_size`: Number of results (default 10, max 100)

## Example Usage

```
Get top headlines from US technology news:
country: "us"
category: "technology"

Search for AI news:
query: "artificial intelligence"
language: "en"
sort_by: "publishedAt"
```