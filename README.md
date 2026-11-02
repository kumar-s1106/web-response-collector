# Web Response Collector
Python learning project that records HTTP response headers, status, requested and final URLs, and UTC collection timestamps in JSON.

# Purpose
This project explores how web response information can support preliminary investigation and documentation. It began as a header checker and was expanded to preserve observations rather than only display them.

## Features
- Accepts a website URL through manual input.
- Adds HTTPS if no protocol is supplied.
- Records the requested URL and final URL after redirects.
- Records request-start and response-recording timestamps in UTC.
- Collects the HTTP status code and response headers.
- Saves observations in a JSON file without overwriting existing files.

## Information Collected

| Field | Description |
|---|---|
| requested_url | Address supplied to the program |
| final_url | Final address reached after redirects |
| request_started_utc | Local UTC timestamp immediately before the request |
| response_recorded_utc | Local UTC timestamp when response metadata is recorded |
| http_status | HTTP response status code |
| headers | Returned header names and values |

## Limitations

- Records only the final response, not the complete redirect chain.
- Does not save the response body or calculate file hashes.
- Does not execute JavaScript or reproduce a complete browser session.
- Does not determine whether a website is safe or malicious.
- Network failures and HTTP errors may currently stop the program.
- Timestamps depend on the accuracy of the computer's clock.
- This is a learning prototype, not a complete forensic acquisition tool.

## Responsible Use

Use the tool for authorised learning and investigation. Requests interact with the target server and may be logged. Review captures before sharing them. Response headers can contain cookies or other sensitive information. Keep original captures separate from any redacted examples.

## Learning Focus

- HTTP requests and response headers
- Python dictionaries and loops
- JSON serialisation and file handling
- Accurate documentation of collected information

## Future Improvements
- Clear error handling
- Redirect-chain recording
- Separate folders for each capture
- Better UI and readability
- Automated analysis of the site for incident response
