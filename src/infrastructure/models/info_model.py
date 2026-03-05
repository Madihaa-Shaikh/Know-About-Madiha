from src.domain.chat_model import ChatModel
from src.infrastructure.config.madiha_profile import MADIHA_PROFILE


class MadihaInfoModel(ChatModel):
    """
    Profile-aware model: answers in CV/portfolio style using MADIHA_PROFILE.
    """

    def reply(self, message: str) -> str:
        msg = (message or "").strip().lower()
        if not msg:
            return "Ask me about Madiha: background, skills, experience, projects, education, or contact."

        # ====== Quick intents ======
        if any(k in msg for k in ["who are you", "about you", "introduce", "summary", "profile", "cv", "resume"]):
            return self._cv_summary()

        if any(k in msg for k in ["experience", "work", "job", "professional", "center for hybrid", "teleseo", "data bites"]):
            return self._experience()

        if any(k in msg for k in ["skills", "stack", "tech", "tools", "technologies"]):
            return self._skills()

        if any(k in msg for k in ["projects", "project", "portfolio"]):
            return self._projects()

        if any(k in msg for k in ["education", "study", "degree", "university", "btu", "mehran"]):
            return self._education()

        if any(k in msg for k in ["publication", "paper", "research"]):
            return self._publications()

        if any(k in msg for k in ["contact", "email", "phone", "linkedin", "github"]):
            return self._contact()

        if any(k in msg for k in ["role", "looking for", "target", "position"]):
            return self._target_roles()

        # Default: helpful menu
        return (
             "Hi how are you ?:\n"
            "I can answer in CV style. Try:\n"
            "• 'Give me a CV summary'\n"
            "• 'What is your experience?'\n"
            "• 'List your skills'\n"
            "• 'Show your projects'\n"
            "• 'Education and research'\n"
            "• 'Contact details'"
        )

    # ====== Responses ======
    def _cv_summary(self) -> str:
        p = MADIHA_PROFILE
        return (
            f"**{p['name']}** — {p['title']}\n"
            f"{p['years_experience']}\n\n"
            f"{p['summary']}\n\n"
            f"**Highlights**\n"
            f"• Real-time RGB-D / 3D perception pipelines (OpenCV / OpenCvSharp)\n"
            f"• Production inference (PyTorch → ONNX → NVIDIA Technologies), GPU-accelerated deployment\n"
            f"• C# gRPC clients with Protocol Buffers for server integration\n"
            f"• 3D data processing: depth maps, point clouds, voxelization\n"
        )

    def _experience(self) -> str:
        p = MADIHA_PROFILE
        out = ["**Professional Experience**\n"]
        for exp in p["experience"]:
            out.append(f"**{exp['company']}** — {exp['role']} ({exp['dates']})")
            for b in exp["bullets"]:
                out.append(f"• {b}")
            out.append("")  # spacer
        return "\n".join(out).strip()

    def _skills(self) -> str:
        p = MADIHA_PROFILE
        s = p["skills"]
        return (
            "**Skills & Tools**\n"
            f"**Programming:** {', '.join(s['programming'])}\n"
            f"**Frameworks:** {', '.join(s['frameworks'])}\n"
            f"**Web:** {', '.join(s['web'])}\n"
            f"**Databases:** {', '.join(s['databases'])}\n"
            f"**AI / CV / DevOps Tools:** {', '.join(s['tools'])}\n"
            f"**Methodologies:** {', '.join(s['methodologies'])}\n"
        )

    def _projects(self) -> str:
        p = MADIHA_PROFILE
        out = ["**Projects**\n"]
        for pr in p["projects"]:
            out.append(f"**{pr['name']}** ({pr['dates']})")
            for b in pr["bullets"]:
                out.append(f"• {b}")
            out.append("")
        return "\n".join(out).strip()

    def _education(self) -> str:
        p = MADIHA_PROFILE
        out = ["**Education**\n"]
        for ed in p["education"]:
            out.append(f"**{ed['degree']}** — {ed['school']} ({ed['dates']})")
            if ed.get("key_skills"):
                out.append(f"• Key skills: {', '.join(ed['key_skills'])}")
            out.append("")
        return "\n".join(out).strip()

    def _publications(self) -> str:
        p = MADIHA_PROFILE
        if not p.get("publications"):
            return "No publications listed."
        out = ["**Publications / Research**\n"]
        for pub in p["publications"]:
            out.append(f"• {pub}")
        return "\n".join(out)

    def _contact(self) -> str:
        p = MADIHA_PROFILE
        c = p["contact"]
        return (
            "**Contact**\n"
            f"• Location: {c['location']}\n"
            f"• Phone: {c['phone']}\n"
            f"• Email: {c['email']}\n"
            f"• LinkedIn: {c['linkedin']}\n"
            f"• GitHub: {c['github']}\n"
        )

    def _target_roles(self) -> str:
        p = MADIHA_PROFILE
        return (
            "**Target Roles**\n"
            + "\n".join([f"• {r}" for r in p["target_roles"]])
        )