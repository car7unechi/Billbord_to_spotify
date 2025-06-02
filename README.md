# 🎶 Billboard Hot 100 Time Machine (Spotify Auto-Player)

This Python project lets you **travel back in time** by entering a specific date (YYYY-MM-DD) and pulling up the **Billboard Hot 100 chart** from that day. Once the list is displayed, you can pick a song by its rank (0–99), and the script will **automatically open it in Spotify** using the Spotify Web API.

---

## 🚀 Features

- Scrapes Billboard's Hot 100 chart for a historical date
- Lists songs and artists in order
- Integrates with the Spotify API to search and play tracks
- Opens tracks automatically in your web browser
- Lets you keep picking songs to listen to until you exit

---

## 🛠️ Tech Stack

- **Python 3**
- **BeautifulSoup** – for web scraping
- **Requests** – for HTTP requests
- **Spotipy** – Python client for the Spotify Web API
- **dotenv** – for securely loading environment variables
- **Webbrowser** – to launch Spotify tracks in your default browser

---

## 📦 Setup & Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/yourusername/hot-100-spotify-player.git
   cd hot-100-spotify-player
