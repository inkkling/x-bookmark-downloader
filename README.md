# X Bookmark Downloader

A Python script that bulk downloads images from your X bookmark folders using X's internal API. No third-party libraries required — just Python.

Built with [Claude Cowork](https://claude.ai) by someone who doesn't code.

---

## What It Does

- Connects to X's internal GraphQL API (the same one the X app itself uses)
- Loops through your specified bookmark folders and pulls every image
- Tracks downloaded images by ID so it never re-downloads duplicates, even if you clear the folder to free up space
- Saves everything organized into subfolders by bookmark folder name
- Logs all activity so you can see what ran and when

---

## Requirements

- **Python 3.x** — [download here](https://www.python.org/downloads/)
  - During install, check **"Add Python to PATH"**
- An X account with at least one bookmark folder
- Your X **auth_token** and **ct0** cookie (instructions below)

No pip installs needed. Uses only Python's built-in libraries.

---

## Files

| File | Purpose |
|---|---|
| `xbd3.py` | Main downloader script |
| `save_creds.py` | One-time setup for your X credentials |
| `Download_X_Bookmarks.bat` | Double-click launcher (Windows only) |

---

## Setup

### Step 1 — Create your folder

Create a folder on your computer and put all three files in it. Example:
```
C:\Users\YourName\Desktop\X Downloader\
```

---

### Step 2 — Set your output path

> ⚠️ **Important:** You need to set `OUTPUT_BASE` in **both** `xbd3.py` and `save_creds.py`. They must match exactly, otherwise the credential setup will save to a different location than where the main script looks.

Open **both files** in Notepad and set `OUTPUT_BASE` to the same path in each.

Example — in `xbd3.py`:
```python
OUTPUT_BASE = r'C:\Users\YourName\Pictures\X Bookmarks'
```

Example — in `save_creds.py`:
```python
OUTPUT_BASE = r'C:\Users\YourName\Pictures\X Bookmarks'
```

This is where your downloaded images and all log files will be saved. The folder will be created automatically if it doesn't exist.

---

### Step 3 — Add your bookmark folders

Still in `xbd3.py`, find this section:
```python
FOLDERS = {
    'Folder Name One': 'YOUR_FOLDER_ID_HERE',
    'Folder Name Two': 'YOUR_FOLDER_ID_HERE',
}
```

Replace `Folder Name One` with whatever you want the local subfolder to be called.
Replace `YOUR_FOLDER_ID_HERE` with your actual X bookmark folder ID.

You can have as many or as few entries as you want — just add or remove lines following the same format. See **How to Find Your Folder IDs** below.

---

### Step 4 — Get your X credentials

You need two cookie values from your browser while logged into X.

1. Go to [x.com](https://x.com) and log in
2. Press **F12** to open Developer Tools
3. Click the **Application** tab
4. In the left sidebar, expand **Cookies** and click `https://x.com`
5. Find `auth_token` in the list — copy its Value column
6. Find `ct0` in the list — copy its Value column

---

### Step 5 — Run save_creds.py

This saves your credentials locally so the main script can use them. You only need to do this once, or again if X logs you out.

1. Open Command Prompt
2. Navigate to your folder:
   ```
   cd C:\Users\YourName\Desktop\X Downloader
   ```
3. Run:
   ```
   python save_creds.py
   ```
4. Paste your `auth_token` and `ct0` when prompted

This creates a `_creds.json` file in your output folder. **Do not share this file or upload it anywhere — it contains your session credentials.**

---

### Step 6 — Run the downloader

Double-click `Download_X_Bookmarks.bat`, or from Command Prompt:
```
python xbd3.py
```

The script will page through each folder, download new images, skip anything already grabbed, and log everything.

---

## How to Find Your Bookmark Folder IDs

X doesn't display folder IDs anywhere in the UI, so you need to pull them from network traffic.

1. Go to [x.com](https://x.com) and open your Bookmarks
2. Press **F12** and click the **Network** tab
3. Filter by **Fetch/XHR**
4. Click into one of your bookmark folders on the page
5. Look for a request containing `BookmarkFolderTimeline` in the network log
6. Click it — the folder ID is the long number in the `bookmark_collection_id` field in the request URL

Repeat for each folder you want to download.

---

## Output Structure

```
Your Output Folder/
├── _creds.json                  ← your saved credentials (keep private)
├── _download_log.json           ← tracks all downloaded image IDs
├── _download_activity.log       ← human-readable log of every run
├── Folder Name One/
│   ├── 1234567890.jpg
│   └── ...
└── Folder Name Two/
    ├── 0987654321.jpg
    └── ...
```

---

## Notes

- **Images only** — photos are downloaded. Videos and GIFs are not currently supported.
- **Credentials expire** — X sessions don't last forever. If you get a 401 error, re-run `save_creds.py` with fresh browser cookies.
- **Rate limiting** — the script includes delays between requests. Don't remove them or you risk hitting X's rate limits.
- **Internal API** — this uses X's unofficial internal API, not a sanctioned public one. X could change it at any time, which may break the script without warning.
- **Personal use only** — this is a backup tool for your own bookmarks. Don't use it to scrape other people's content.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| Output folder not found | Check `OUTPUT_BASE` in `xbd3.py` is a valid path, or create the folder manually first |
| Auth failed / 401 error | Credentials expired — re-run `save_creds.py` with fresh cookies from your browser |
| `_creds.json` is missing | You haven't run `save_creds.py` yet, or `OUTPUT_BASE` doesn't match between the two files |
| Downloads 0 images | Your folder IDs are likely wrong — double-check them using the network method above |
| `python` not recognized | Python isn't installed, or wasn't added to PATH during install |

---

## Credits

Built by [@noravoid_log](https://x.com/noravoid_log) with [Claude Cowork](https://claude.ai). No prior coding knowledge required or used.
