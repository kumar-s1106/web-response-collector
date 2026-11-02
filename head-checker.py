import json
from datetime import datetime, timezone
import urllib.request

url = input("Enter a website URL: ").strip()

if not url.startswith(("http://", "https://")):
    url = "https://" + url

started_at = datetime.now(timezone.utc)

with urllib.request.urlopen(url, timeout=10) as response:
    print("Status:", response.status)

    evidence = {
        "requested_url": url,
        "final_url": response.geturl(),
        "request_started_utc": started_at.isoformat(),
        "response_recorded_utc": datetime.now(timezone.utc).isoformat(),
        "http_status": response.status,
        "headers": list(response.headers.items())
    }

    filename = started_at.strftime("capture_%Y%m%dT%H%M%S_%fZ.json")

    with open(filename, "x", encoding="utf-8") as file:
        json.dump(evidence, file, indent=4)

    print("Final URL:", response.geturl())
    print("Headers collected:", len(evidence["headers"]))
    print("Full headers saved in:", filename)

    print("\nResponse record saved to:", filename)
