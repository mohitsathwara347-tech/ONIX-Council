from client import call_model
from config import MEMBERS

MAX_ROUNDS = 5

def iterative_council(topic, stream_callback=None):
    draft = ""
    round_no = 1
    discussion_log = ""

    def emit(text):
        nonlocal discussion_log
        discussion_log += text + "\n\n"
        if stream_callback:
            stream_callback(discussion_log)

    while round_no <= MAX_ROUNDS:
        emit(f"🔄 **ROUND {round_no}**")
        satisfied_members = 0

        for member in MEMBERS:
            emit(f"🧠 **{member['name']} reviewing...**")

            messages = [
                {
                    "role": "system",
                    "content": (
                        f"You are {member['name']} in an AI council.\n"
                        "You collaboratively refine a shared explanation.\n\n"
                        "If the draft is acceptable, reply EXACTLY with:\n"
                        "SATISFIED\n\n"
                        "If not, improve the draft and end with:\n"
                        "NOT SATISFIED"
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"Topic: {topic}\n\n"
                        f"Current Draft:\n{draft if draft else '[EMPTY]'}"
                    )
                }
            ]

            response = call_model(
                member["api_key"],
                member["model"],
                messages
            )

            emit(response)

            if "SATISFIED" in response.upper():
                satisfied_members += 1
            else:
                draft = response

        if satisfied_members == len(MEMBERS):
            emit("✅ **All members are satisfied.**")
            break

        round_no += 1

    return draft, discussion_log
