# Insta Unfollowers

A simple Python tool to find people you follow on Instagram who **don't follow you back**.  
This can help you clean up your following list and identify ghost followers.

## 🔍 Features

- Parses your Instagram `followers.json` and `following.json` data exports
- Detects users who don't follow you back
- Outputs the list of non-followers with profile links to a JSON file
- Clean and readable codebase, easy to customize

## 📁 File Structure

```
📦insta-unfollowers
 ┣ 📄main.py
 ┣ 📄followers.json        ← Instagram followers data
 ┣ 📄following.json        ← Instagram following data
 ┗ 📄non_followers.json    ← Output file with people not following you back
```

## 🚀 How to Use

### 1. Export Your Instagram Data

Go to your Instagram app or website:

- **Profile → Settings → Your activity → Download your information**
- Request a **JSON** format export
- Unzip the downloaded file and locate:
  - `followers.json`
  - `following.json`

### 2. Place Files

Copy both `followers.json` and `following.json` into the same directory as `main.py`.

### 3. Run the Script

Make sure you have Python installed. Then run:

```bash
python main.py
```

### 4. View Results

After execution, you'll find a new file named `non_followers.json` containing a list of profile links for people who don’t follow you back.

---

## 📌 Example Output

```json
{
  "non_followers": [
    "https://www.instagram.com/username1/",
    "https://www.instagram.com/username2/"
  ]
}
```

---

## 🧠 How It Works

- Parses both JSON files to extract usernames.
- Compares your “following” list against your “followers”.
- Any account you're following but isn't in your followers list gets added to the result.

---

## ⚠️ Disclaimer

This tool works with Instagram's data export format. Instagram may change how data is structured, so the script might need updates in the future.

We don't collect or store your data — everything runs locally on your machine.

---

## 📄 License

MIT License  
Feel free to fork, modify, or use this project as you like!

---

## 💡 Ideas for Future Enhancements

- Web-based version
- GUI support
- Export to CSV
- Detect mutual followers
- Scheduled unfollower checks

---

Made with ❤️ in Python
