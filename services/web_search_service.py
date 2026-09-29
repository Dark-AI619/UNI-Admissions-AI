import json
import os
from urllib import request, error

SERPER_ENDPOINT = "https://google.serper.dev/search"

def _get_serper_key() -> str:
    key = os.getenv("SERPER_API_KEY", "").strip()
    if not key:
        try:
            import streamlit as st
            key = str(st.secrets.get("SERPER_API_KEY", "")).strip()
        except Exception:
            key = ""
    if not key:
        raise RuntimeError("SERPER_API_KEY is missing. Add it to Streamlit Secrets.")
    return key

def serper_search(query: str, num: int = 8) -> list[dict]:
    payload = json.dumps({"q": query, "num": num}).encode("utf-8")
    req = request.Request(
        SERPER_ENDPOINT,
        data=payload,
        headers={
            "X-API-KEY": _get_serper_key(),
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Serper search failed ({exc.code}): {body}") from exc
    except Exception as exc:
        raise RuntimeError(f"Serper search failed: {exc}") from exc

    results = []
    for item in data.get("organic", [])[:num]:
        results.append({
            "title": item.get("title", ""),
            "url": item.get("link", ""),
            "snippet": item.get("snippet", ""),
        })
    return results

def build_admissions_research(student_profile: str) -> str:
    queries = [
        f"{student_profile}\n official university admissions requirements international students",
        f"{student_profile}\n official scholarship requirements university international students",
    ]
    blocks = []
    for query in queries:
        rows = serper_search(query, num=8)
        blocks.append(f"SEARCH QUERY:\n{query}\n")
        for i, row in enumerate(rows, 1):
            blocks.append(
                f"[{i}] {row['title']}\nURL: {row['url']}\nSnippet: {row['snippet']}\n"
            )
    return "\n".join(blocks)
