import os

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Hello Aakash</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <h1>Hi Aakash</h1>
</body>
</html>
"""

CSS = """body {
  margin: 0;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #0f1115;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Helvetica, Arial, sans-serif;
}

h1 {
  color: #e8eaed;
  font-size: 3rem;
}
"""


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(HTML)

    with open(os.path.join(OUTPUT_DIR, "style.css"), "w", encoding="utf-8") as f:
        f.write(CSS)

    print(f"Site generated in: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
