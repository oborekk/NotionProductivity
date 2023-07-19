# NotionProductivity
This little Python script connects to the Notion API and fetches data from a database within my Productivity Tracking page.

It sanitizes the data for matplotlib, and generates a linechart.

Since the Notion API does not support direct binary uploads, the image is loaded from an URL that redirects to the docker container where this script is executed daily.
