🗣️ Voice Assistant (Beginner Level)

This is a simple **Python Voice Assistant** that listens to your voice commands and performs basic tasks like telling the time, date, searching the web, and fetching information from Wikipedia.

---

## 🚀 Features

✅ Responds to greetings  
✅ Tells the current **time** and **date**  
✅ Searches anything on **Google**  
✅ Reads short **Wikipedia summaries**  
✅ Simple **speech-to-text** and **text-to-speech** interaction  
✅ Works entirely **offline** (except Wikipedia/Google search)

---

## 🧰 Requirements

Make sure you have **Python 3.12+** installed.  
Then install the required libraries using this command:

```bash
python -m pip install SpeechRecognition pyttsx3 wikipedia requests
```

You’ll also need a **microphone** connected to your computer.

---

## 📂 Project Structure

```
voice_assistant_basic/
│
├── voice_assistant_basic.py   # Main Python file
└── README.md                  # Documentation file
```

---

## ▶️ How to Run

1. Open the project folder in **VS Code** or terminal  
2. Run the Python script:

   ```bash
   python voice_assistant_basic.py
   ```

3. Speak into your microphone when prompted with “Listening…”

---

## 🗨️ Example Commands

Try saying any of these:

- “Hello”
- “What’s the time?”
- “What’s today’s date?”
- “Search Python programming”
- “Wikipedia Elon Musk”
- “Bye”

---

## ⚙️ How It Works

- Uses `SpeechRecognition` to capture and convert voice → text  
- Uses `pyttsx3` to convert text → speech  
- Integrates with **Wikipedia API** and **Google Search**  
- Simple control loop for continuous listening until you say “Bye”

---

## 🧠 Future Enhancements (Advanced Version)

Once you’re ready for the advanced version, you can add:
- 🎧 Wake word (e.g. “Hey Assistant”)
- 📧 Email sending feature
- 🌦️ Weather updates via OpenWeather API
- 🤖 NLP-based conversation

---

## 👩‍💻 Author

**Sadia Usman**  
Beginner Python Developer — passionate about AI & automation 💡  
