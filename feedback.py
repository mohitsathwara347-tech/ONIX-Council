from client import call_model
from config import MEMBERS

def collect_final_feedback(topic, final_draft):
    feedbacks = []

    print("\n📝 Collecting final individual feedbacks...\n")

    for member in MEMBERS:
        print(f"💬 {member['name']} giving final feedback...")

        messages = [
            {
                "role": "system",
                "content": (
                    f"You are {member['name']}.\n"
                    "The council has reached consensus.\n"
                    "Provide your FINAL individual feedback.\n\n"
                    "Include:\n"
                    "1. Whether you agree with the final draft\n"
                    "2. One strength\n"
                    "3. One limitation or caveat (if any)\n\n"
                    "Do NOT rewrite the draft."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Topic: {topic}\n\n"
                    f"Final Draft:\n{final_draft}"
                )
            }
        ]

        response = call_model(
            member["api_key"],
            member["model"],
            messages
        )

        feedbacks.append({
            "name": member["name"],
            "feedback": response
        })

    return feedbacks
