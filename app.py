import os
from flask import Flask, request, jsonify
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from groq import Groq

# https://api.slack.com/apps/A08GZACKWBT/install-on-team
SLACK_BOT_TOKEN = "xoxb-858xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxzGg"

# https://console.groq.com/keys
GROQ_API_KEY = 'gsk_5rxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxRPf'

# Initialize Slack and Groq clients
slack_client = WebClient(token=SLACK_BOT_TOKEN)
client = Groq(api_key=GROQ_API_KEY)

# Get Bot's User ID to prevent self-replies
bot_user_id = slack_client.auth_test()["user_id"]

# Flask app
app = Flask(__name__)

def generate_reply(message_text):
    """Generate AI-based reply using Groq."""
    try:
        completion = client.chat.completions.create(
            model="llama-3.2-1b-preview",
            messages=[{"role": "user", "content": message_text}],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=False,
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        return "Sorry, I'm having trouble processing your request."

@app.route("/slack/events", methods=["POST"])
def slack_events():
    """Slack webhook endpoint to receive real-time messages."""
    data = request.json

    # Slack URL Verification (Required during setup)
    if "challenge" in data:
        return jsonify({"challenge": data["challenge"]})

    # Process Incoming Message Events
    if "event" in data:
        event = data["event"]
        event_type = event.get("type")

        if event_type == "message" and "subtype" not in event:
            user = event.get("user")
            text = event.get("text")
            channel = event.get("channel")

            # ✅ Prevent bot from replying to itself
            if user == bot_user_id:
                print("⚠️ Ignoring bot's own message.")
                return jsonify({"status": "ignored"}), 200

            print(f"📩 New Message from {user}: {text}")

            # Generate reply and send response
            reply = generate_reply(text)
            send_slack_message(channel, reply)

    return jsonify({"status": "ok"}), 200

@app.route("/send_message", methods=["POST"])
def api_send_message():
    """API to send a Slack message."""
    data = request.json
    channel = data.get("channel")
    message = data.get("message")

    if not channel or not message:
        return jsonify({"error": "Missing 'channel' or 'message' parameter"}), 400

    try:
        response = send_slack_message(channel, message)
        return jsonify({"success": True, "message": "Message sent!", "response": response.data})
    except SlackApiError as e:
        return jsonify({"success": False, "error": str(e.response['error'])}), 500

def send_slack_message(channel, text):
    """Function to send a message to Slack."""
    try:
        response = slack_client.chat_postMessage(
            channel=channel,
            text=text
        )
        return response
    except SlackApiError as e:
        print(f"⚠️ Error sending message: {e.response['error']}")
        raise

@app.route("/fetch_messages", methods=["GET"])
def fetch_messages():
    """API to fetch real-time messages from a Slack channel."""
    channel_id = request.args.get("channel")

    if not channel_id:
        return jsonify({"error": "Missing 'channel' parameter"}), 400

    try:
        response = slack_client.conversations_history(channel=channel_id, limit=10)
        messages = response["messages"]

        return jsonify({"success": True, "messages": messages})

    except SlackApiError as e:
        return jsonify({"success": False, "error": str(e.response['error'])}), 500

if __name__ == "__main__":
    app.run(port=3000, debug=True)
