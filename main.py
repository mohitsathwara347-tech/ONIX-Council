from iterative_council import iterative_council
from council import chairman_conclusion
from feedback import collect_final_feedback

if __name__ == "__main__":
    topic = input("📝 Enter topic: ")

    print("\n🏛️ Council deliberation started...")
    final_draft = iterative_council(topic)

    # Final individual feedbacks
    feedbacks = collect_final_feedback(topic, final_draft)

    print("\n📢 FINAL INDIVIDUAL FEEDBACKS:\n")
    for fb in feedbacks:
        print(f"--- {fb['name']} ---")
        print(fb["feedback"])
        print()

    # Chairman conclusion
    print("👑 Chairman concluding...\n")
    conclusion = chairman_conclusion(topic, final_draft)

    print("📌 FINAL CONCLUSION:\n")
    print(conclusion)
