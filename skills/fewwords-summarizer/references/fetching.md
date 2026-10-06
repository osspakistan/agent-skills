# Fetching Content

> [!CAUTION]
> **DO NOT use built-in browser or `web_fetch` tools.** Built-in fetch tools enforce strict site restrictions, get blocked by robots.txt, or hallucinate using Google search snippet text. 
> Always execute `curl` commands in bash as specified below.

When the user provides a URL instead of raw text, extract the content before doing anything else. Use markdown proxy services first, then fall back to direct fetch.

---

## Strategy 1: Markdown Conversion Proxies (Recommended)

Both **`curl.md`** and **`r.jina.ai`** convert any web page directly into clean, readable Markdown by stripping navigation, ads, headers, and clutter.

### Option A: `curl.md` (Fast, clean Markdown with frontmatter)
Prepend `https://curl.md/` to the target URL:

```bash
curl -sL "https://curl.md/<TARGET_URL>"
```

**Example:**
```bash
curl -sL "https://curl.md/https://example.com/blog/ai-future"
```

### Option B: `r.jina.ai` (Jina Reader API)
Prepend `https://r.jina.ai/` to the target URL:

```bash
curl -sL "https://r.jina.ai/<TARGET_URL>"
```

**Options & Tokens (if available):**
```bash
# Plain text format
curl -sL -H "Accept: text/plain" "https://r.jina.ai/<TARGET_URL>"

# With API key if set in environment
curl -sL -H "Authorization: Bearer $JINA_AI_API_KEY" "https://r.jina.ai/<TARGET_URL>"
```

---

## Strategy 2: Direct `curl` (Fallback)

If both `curl.md` and `r.jina.ai` fail, timeout, or are blocked, fetch the URL directly:

```bash
curl -sL \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" \
  "<TARGET_URL>"
```

- `-s`: Silent mode (no progress bar)
- `-L`: Follow HTTP redirects automatically

---

## Strategy 3: YouTube Links

For YouTube URLs (`youtube.com/watch?v=...` or `youtu.be/...`):
1. **Captions / Transcripts first:** Use transcript tools or `yt-dlp` if available (`yt-dlp --write-sub --skip-download`).
2. **Proxy Fallback:** Run `curl -sL "https://r.jina.ai/<YOUTUBE_URL>"` or `curl -sL "https://curl.md/<YOUTUBE_URL>"` to fetch video metadata, title, and description.

---

## Failure Handling

If all extraction methods return empty content, HTTP 403, Cloudflare challenge, or bot-block errors:
> *"This URL is paywalled or protected against scraping. Please paste the article text or video transcript directly and I will summarize it."*
