import streamlit as st

from iterative_council import iterative_council
from feedback import collect_final_feedback
from council import chairman_conclusion

st.set_page_config(page_title="AI Council", layout="wide")
st.title("🏛️ AI Council – Live Deliberation")

# ---------------- SESSION STATE ----------------
if "discussion" not in st.session_state:
    st.session_state.discussion = ""

if "final_answer" not in st.session_state:
    st.session_state.final_answer = ""

if "feedbacks" not in st.session_state:
    st.session_state.feedbacks = []

if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- INPUT ----------------
topic = st.text_input("📝 Ask the Council a Topic")

# ---------------- UI PLACEHOLDERS ----------------
left, center, right = st.columns([1.2, 1.6, 1.2])

discussion_box = left.empty()
chairman_box = center.empty()
feedback_box = right.empty()

def stream_to_ui(text):
    discussion_box.markdown(text)

if st.button("Send to Council") and topic.strip():
    st.session_state.discussion = ""
    st.session_state.final_answer = ""
    st.session_state.feedbacks = []

    with st.spinner("Council is deliberating live..."):
        final_draft, full_discussion = iterative_council(
            topic,
            stream_callback=stream_to_ui
        )

        # Collect feedback
        feedbacks = collect_final_feedback(topic, final_draft)

        # Chairman decision
        final_answer = chairman_conclusion(topic, final_draft)

        st.session_state.discussion = full_discussion
        st.session_state.feedbacks = feedbacks
        st.session_state.final_answer = final_answer
        st.session_state.history.append(topic)

# ---------------- RENDER FINAL SECTIONS ----------------
with center:
    st.subheader("👑 Chairman's Final Answer")
    if st.session_state.final_answer:
        st.success(st.session_state.final_answer)
    else:
        st.info("Waiting for chairman conclusion...")

with right:
    st.subheader("🧠 Member Final Feedbacks")
    if st.session_state.feedbacks:
        for fb in st.session_state.feedbacks:
            with st.expander(fb["name"]):
                st.write(fb["feedback"])
    else:
        st.info("Feedback will appear after consensus.")

# ---------------- HISTORY ----------------
st.divider()
st.subheader("📜 Previous Questions")
for i, q in enumerate(reversed(st.session_state.history), 1):
    st.write(f"{i}. {q}")
