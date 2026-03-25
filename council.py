from client import call_model
from config import CHAIRMAN

def chairman_conclusion(topic, final_draft):
    messages = [
        {
            "role": "system",
            "content": (
                "You are the Chairman of the AI Council.\n"
                "All members have reached consensus.\n"
                "Your task:\n"
                "1. Improve clarity\n"
                "2. Remove redundancy\n"
                "3. Provide a final authoritative conclusion"
            )
        },
        {
            "role": "user",
            "content": (
                f"Topic: {topic}\n\n"
                f"Final Agreed Draft:\n{final_draft}"
            )
        }
    ]

    return call_model(
        CHAIRMAN["api_key"],
        CHAIRMAN["model"],
        messages
    )
