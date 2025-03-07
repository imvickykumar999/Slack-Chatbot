># `Slack Chatbot`
>
>![image](https://github.com/user-attachments/assets/31dd86ac-a379-4dcb-9b48-e8e87c59a7db)
# **Slack Chatbot with Real-Time Webhook & AI Replies – Setup Guide**  

This guide provides step-by-step instructions to set up a **Slack chatbot** from scratch, integrate it with **Slack API**, enable **real-time messaging via webhooks**, and add **AI-powered replies** using **Groq API**.

---

## **1️⃣ Prerequisites**
Before starting, ensure you have:
- **Slack workspace** ([Sign up](https://slack.com/get-started))
- **Slack API App** ([Create here](https://api.slack.com/apps))
- **Python 3.7+** installed
- **Ngrok** ([Download](https://ngrok.com/download)) for local testing
- **Groq API key** ([Sign up](https://groq.com))

---

## **2️⃣ Create a Slack App**
### **Step 1: Go to Slack API**
- Visit [Slack API Apps](https://api.slack.com/apps)
- Click **"Create New App"**
- Select **"From Scratch"**
- Enter:
  - **App Name**: `Chatbot`
  - **Workspace**: Select your Slack workspace
- Click **Create App**

---

## **3️⃣ Enable Bot User & Permissions**
### **Step 2: Add a Bot User**
- Navigate to **"App Home"** (left menu)
- Under **"Your App's Presence in Slack"**, enable:
  - ✅ **Always Show My Bot**
  - ✅ **Allow Users to DM the Bot**
- Click **"Save Changes"**

### **Step 3: Configure Bot Permissions**
- Go to **"OAuth & Permissions"** (left menu)
- Scroll down to **"Bot Token Scopes"**
- Click **"Add an OAuth Scope"** and add:
  - ✅ `chat:write` – Send messages as the bot
  - ✅ `chat:write.public` – Send messages to public channels
  - ✅ `im:write` – Send direct messages
  - ✅ `im:history` – Read messages from direct messages
  - ✅ `channels:join` – Join public channels
  - ✅ `groups:write` – Manage private channels
- Click **"Save Changes"**

### **Step 4: Install the App**
- Scroll up to **"OAuth Tokens for Your Workspace"**
- Click **"Install App to Workspace"**
- **Authorize** the app
- **Copy the "Bot User OAuth Token" (`xoxb-...`)**  
  *(You'll need this later.)*

---

## **4️⃣ Set Up Real-Time Event Subscriptions**
### **Step 5: Enable Event Subscriptions**
- Go to **"Event Subscriptions"** (left menu)
- Toggle **"Enable Events"**
- In **"Request URL"**, enter:
  ```
  https://your-ngrok-url.ngrok.io/slack/events
  ```
  *(We'll set up `ngrok` in step 7.)*

### **Step 6: Subscribe to Bot Events**
- Scroll to **"Subscribe to Bot Events"**
- Click **"Add Bot User Event"**, then add:
  - ✅ `message.channels` – Messages in public channels
  - ✅ `message.groups` – Messages in private channels
  - ✅ `message.im` – Direct messages
  - ✅ `message.mpim` – Group DMs
- Click **"Save Changes"**
- Reinstall the app if required.

---

## **5️⃣ Set Up Ngrok (For Local Testing)**
### **Step 7: Install & Start Ngrok**
- **Install Ngrok** (if not installed):
  - Windows: [Download](https://ngrok.com/download)
  - Mac/Linux:
    ```sh
    brew install ngrok  # macOS
    sudo apt install ngrok  # Ubuntu
    ```
- **Run Ngrok**:
  ```sh
  ngrok http 3000
  ```
- Copy the **public URL** (e.g., `https://your-ngrok-url.ngrok.io`)  
- **Update Slack's "Request URL"** (from Step 5).

---

## **6️⃣ Get Your Groq API Key**
### **Step 8: Sign Up for Groq**
- Visit [Groq API](https://groq.com)
- Sign up and log in
- Navigate to **API Keys** and **generate a new API key**
- Copy the **API key (`gsk_...`)** for later use

---

## **7️⃣ Run Your Slack Chatbot**
### **Step 9: Start the Flask Server**
- Open a terminal and navigate to the bot's project folder
- Run the bot:
  ```sh
  python3 main.py
  ```
- You should see:
  ```
  Running on http://127.0.0.1:3000
  ```

---

## **8️⃣ Test Your Bot**
### **Step 10: Send a Message to the Bot**
- Open **Slack**
- Go to **Direct Messages**
- Select **Chatbot**
- Send **"Hello bot!"**
- **The bot should reply automatically! 🎉**

---

## **9️⃣ Troubleshooting**
### **Issue: Bot Not Responding?**
✔️ **Check Slack Permissions**: Ensure you added correct scopes  
✔️ **Check Ngrok**: Restart `ngrok` if the request URL is not working  
✔️ **Check Flask Logs**: Run `python3 main.py` and look for errors  
✔️ **Reinstall App**: Go to **OAuth & Permissions → Reinstall App to Workspace**  

---

## **🎯 Next Steps**
- Deploy your bot on **AWS/GCP/Heroku** for 24/7 availability  
- Integrate with **Slack interactive buttons & commands**  
- Add **custom AI responses using Groq API**  

---

### **🚀 Your Slack Bot is Now Live! Enjoy Real-time AI Conversations!** 🎉  
Let me know if you need any modifications! 😊
