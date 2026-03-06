import requests
from src.domain.chat_model import ChatModel
from src.infrastructure.config.madiha_profile import MADIHA_PROFILE


class GeneralChatModel(ChatModel):
    def __init__(self, model_name: str = "phi3:latest"):
        self.model_name = model_name
        self.url = "http://localhost:11434/api/chat"

        self.system_message = """
            You are a helpful, friendly, and professional assistant.

            Rules:
            - Answer general user questions clearly and naturally.
            - Do NOT invent or guess any personal, educational, or professional facts about Madiha.
            - Do NOT describe Madiha's background, degree, university, projects, experience, or skills unless that information is explicitly returned by the profile-specific logic.
            - If the user asks a general question, answer it normally and briefly.
            - After your general answer, you may add a short teaser saying that you can also share Madiha's background, skills, projects, or experience.
            - Never make up details such as universities, companies, degrees, publications, or achievements.
            - If information about Madiha is requested, that should be handled only by the dedicated profile logic.
            """

    def reply(self, message: str) -> str:
        msg = (message or "").strip()
        if not msg:
            return "Please type something."

        # 1) Direct Madiha-related intent
        intent = self._detect_madiha_intent(msg)
        if intent == "summary":
            return self._madiha_summary()
        if intent == "experience":
            return self._madiha_experience()
        if intent == "skills":
            return self._madiha_skills()
        if intent == "projects":
            return self._madiha_projects()
        if intent == "education":
            return self._madiha_education()
        if intent == "contact":
            return self._madiha_contact()
        if intent == "roles":
            return self._madiha_roles()

        # 2) Normal general reply + teaser
        try:
            payload = {
                "model": self.model_name,
                "messages": [
                    {"role": "system", "content": self.system_message},
                    {"role": "user", "content": msg}
                ],
                "stream": False
            }

            r = requests.post(self.url, json=payload, timeout=60)
            r.raise_for_status()
            data = r.json()

            base_reply = data["message"]["content"].strip()
            return base_reply + self._madiha_intro_teaser()

        except Exception as e:
            return (
                "Couldn't reach Ollama at http://localhost:11434.\n"
                "Make sure Ollama is running.\n\n"
                f"Error: {e}"
            )

    # -----------------------------
    # Intent detection
    # -----------------------------
    def _detect_madiha_intent(self, message: str) -> str | None:
        msg = message.lower()

        if any(k in msg for k in [
            "who is madiha", "about madiha", "introduce madiha", "tell me about madiha",
            "who are you", "about you", "introduce yourself", "background", "cv", "resume", "profile", "summary"
        ]):
            return "summary"

        if any(k in msg for k in [
            "experience", "years of experience", "how many years", "work experience",
            "professional experience", "job", "where have you worked", "projects", "portfolio"
        ]):
            return "experience"

        if any(k in msg for k in [
            "skills", "tech stack", "tools", "technologies", "what can you do"
        ]):
            return "skills"

        if any(k in msg for k in [
            "projects", "project", "portfolio", "what have you built", "show projects"
        ]):
            return "projects"

        if any(k in msg for k in [
            "education", "study", "degree", "university", "btu", "mehran","certification", "certificate"
        ]):
            return "education"

        if any(k in msg for k in [
            "contact", "email", "phone", "linkedin", "github"
        ]):
            return "contact"

        if any(k in msg for k in [
            "looking for", "target roles", "career goals", "positions", "job roles"
        ]):
            return "roles"

        return None

    # -----------------------------
    # Teaser for general questions
    # -----------------------------
    def _madiha_intro_teaser(self) -> str:
        return (
            "\n\nIf you'd like, I can also tell you more about Madiha's background, "
            "skills, projects, professional experience, education, or contact details."
        )

    # -----------------------------
    # Madiha profile responses
    # -----------------------------
    def _madiha_summary(self) -> str:
        return (
            "Hi! I'm Madiha Shaikh.\n\n"
            "I'm an AI Engineer with over 5 years of industry experience in Software Engineering and Applied AI. "
            "My work focuses on Computer Vision, 3D perception, intelligent AI systems, and production-ready AI deployment.\n\n"
            "I completed my Master’s degree in Artificial Intelligence at Brandenburg University of Technology (BTU), Germany, in April 2026.\n\n"
            "I’ve worked with technologies such as PyTorch, ONNX, NVIDIA inference technologies, LLM systems, Ollama, "
            "RAG pipelines, LangChain, APIs, microservices, and containerized AI environments.\n\n"
            "You can ask me about my skills, professional experience, projects, education, or career goals."
        )

    def _madiha_experience(self) -> str:
        p = MADIHA_PROFILE
        out = [
            "I have over 5 years of professional experience in Software Engineering and Applied AI.\n",
            "Here is a quick overview of my professional experience:\n"
        ]

        for exp in p["experience"]:
            out.append(f"**{exp['company']}** — {exp['role']} ({exp['dates']})")
            for b in exp["bullets"]:
                out.append(f"• {b}")
            out.append("")

        return "\n".join(out).strip()

    def _madiha_skills(self) -> str:
        s = MADIHA_PROFILE["skills"]
        return (
            "Here are some of my core skills:\n\n"
            f"**Programming:** {', '.join(s['programming'])}\n"
            f"**Frameworks:** {', '.join(s['frameworks'])}\n"
            f"**Web:** {', '.join(s['web'])}\n"
            f"**Databases:** {', '.join(s['databases'])}\n"
            f"**AI / CV / DevOps Tools:** {', '.join(s['tools'])}\n"
            f"**Methodologies:** {', '.join(s['methodologies'])}"
        )

    def _madiha_projects(self) -> str:
        out = ["Here are some of the projects I’ve worked on:\n"]
        for pr in MADIHA_PROFILE["projects"]:
            out.append(f"**{pr['name']}** ({pr['dates']})")
            for b in pr["bullets"]:
                out.append(f"• {b}")
            out.append("")
        return "\n".join(out).strip()

    def _madiha_education(self) -> str:
        p = MADIHA_PROFILE

        out = ["Here is my educational background:\n"]

        for ed in p["education"]:
            out.append(f"**{ed['degree']}**")
            out.append(f"{ed['school']} ({ed['dates']})")

            if ed.get("key_skills"):
                out.append(f"Focus Areas: {', '.join(ed['key_skills'])}")

            out.append("")

        # certifications
        if p.get("certifications"):
            out.append("**Certifications:**\n")

            for c in p["certifications"]:
                out.append(f"• {c['name']} — {c['provider']} ({c['date']})")

        out.append("\nYou can also ask me about my projects, skills, or professional experience.")

        return "\n".join(out).strip()

    def _madiha_contact(self) -> str:
        c = MADIHA_PROFILE["contact"]
        return (
            "You can reach me through the following contact details:\n\n"
            f"• Location: {c['location']}\n"
            f"• Phone: {c['phone']}\n"
            f"• Email: {c['email']}\n"
            f"• LinkedIn: {c['linkedin']}\n"
            f"• GitHub: {c['github']}"
        )

    def _madiha_roles(self) -> str:
        roles = MADIHA_PROFILE["target_roles"]
        return (
            "I am currently interested in opportunities such as:\n\n"
            + "\n".join([f"• {r}" for r in roles])
        )