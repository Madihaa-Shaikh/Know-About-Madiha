import gradio as gr

from src.infrastructure.models.info_model import MadihaInfoModel
from src.infrastructure.models.general_model import GeneralChatModel
from src.application.chat_router import ChatRouter

# -----------------------
# Clean Architecture: DI
# -----------------------
router = ChatRouter(
    info_model=MadihaInfoModel(),
    general_model=GeneralChatModel()
)

def chat_fn(message, mode, history):
    history = history or []

    if not message or not message.strip():
        return history

    answer = router.reply(message, mode)

    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": answer})

    return history

def clear_chat():
    return []

# -----------------------
# UI Theme + CSS
# -----------------------
theme = gr.themes.Soft(
    primary_hue="orange",
    radius_size="lg",
    font=[gr.themes.GoogleFont("Inter"), "ui-sans-serif", "system-ui"]
)

css = """
#wrap { max-width: 980px; margin: 0 auto; }
.hero {
  padding: 18px 18px;
  border-radius: 18px;
  border: 1px solid rgba(255,255,255,0.10);
  background: linear-gradient(135deg, rgba(255,165,0,0.18), rgba(255,255,255,0.04));
}
.hero-title {
  font-size: 30px;
  font-weight: 800;
  letter-spacing: 0.2px;
  line-height: 1.1;
}
.hero-sub {
  margin-top: 8px;
  opacity: 0.85;
  font-size: 14px;
}
.badges { display:flex; gap:10px; flex-wrap:wrap; margin-top:12px; }
.badge {
  font-size: 12px;
  padding: 6px 10px;
  border-radius: 999px;
  border: 1px solid rgba(255,255,255,0.14);
  background: rgba(255,255,255,0.06);
  color:red;
}
.section-label { margin-top: 14px; opacity: 0.85; font-size: 12px; }
"""

# -----------------------
# UI Layout
# -----------------------
with gr.Blocks(title="Know About Madiha") as demo:
    with gr.Column(elem_id="wrap"):
        gr.HTML("""
            <div class="hero">

        <div class="hero-title">
            Know About Madiha
        </div>

        <div class="hero-sub">
            <b>Available models</b><br>
            • <b>Madiha</b> – Ask about Madiha's profile<br>
            • <b>phi3</b> – General AI assistant
        </div>

        <div class="hero-sub" style="margin-top:12px;">
            <b>You can ask questions like:</b><br>
            • Who is Madiha?<br>
            • Give me a CV summary<br>
            • What are Madiha's skills?<br>
            • Show Madiha's projects<br>
            • What is Madiha's work experience?<br>
            • How can I contact Madiha?
        </div>

        <div class="badges" style="margin-top:14px;">
            <span class="badge">CV</span>
            <span class="badge">Skills</span>
            <span class="badge">Projects</span>
            <span class="badge">Experience</span>
            <span class="badge">Education</span>
        </div>

        </div>
        """)

        gr.Markdown('<div class="section-label">SETTINGS</div>')
        with gr.Row():
            mode = gr.Dropdown(
                choices=["I am Madiha (talk to me)", "General Chat"],
                value="General Chat",
                label="Mode",
                scale=4
            )

        
        
        gr.Markdown('<div class="section-label">CHAT</div>')
        chatbot = gr.Chatbot(label="", height=460)
        
        with gr.Row():
            msg = gr.Textbox(
                label="Message",
                placeholder="Type a message… (Press Enter or click Send)",
                lines=2,
                scale=8
            )

            with gr.Column(scale=1, elem_id="btncol"):
                send_btn = gr.Button("Send", variant="primary")
                clear_btn = gr.Button("Clear", variant="secondary")


        # Enter + Send
        msg.submit(chat_fn, [msg, mode, chatbot], chatbot)
        send_btn.click(chat_fn, [msg, mode, chatbot], chatbot)

        # Clear input after send
        msg.submit(lambda: "", None, msg)
        send_btn.click(lambda: "", None, msg)

        # Clear chat
        clear_btn.click(clear_chat, None, chatbot)

        # Reset chat when mode changes
        mode.change(clear_chat, None, chatbot)

# Gradio 6: theme/css must be passed in launch()
demo.launch(theme=theme, css=css)




theme = gr.themes.Soft()

css = """
#msgrow {
  align-items: stretch !important;
  gap: 12px;
}

#btncol {
  display: flex;
  flex-direction: column;
  height: 100%;
  justify-content: space-between;
}

#btncol button {
  flex: 1;
}

#btncol button + button {
  margin-top: 10px;
}
"""

demo.launch(theme=theme, css=css)
