"""A small, explainable campus FAQ assistant with source-aware retrieval."""
from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass
class FAQ:
    question: str
    answer: str
    source: str


KNOWLEDGE_BASE = [
    FAQ("How do I reset my student portal password?", "Use the 'Forgot password' link on the student portal sign-in page. If the reset email does not arrive, contact the IT help desk.", "Student IT guide, section 2"),
    FAQ("When is the library open?", "The library is open Monday to Saturday, 8:00 AM to 9:00 PM. Sunday hours are 10:00 AM to 4:00 PM during term time.", "Library hours notice, updated August 2026"),
    FAQ("Where can I get my student ID card?", "Visit the student services desk in the main administration building with a photo ID. Replacement cards may have a fee.", "Student services handbook, section 4"),
    FAQ("How do I apply for an internship letter?", "Submit the internship letter request form to the placement office at least five working days before you need the letter.", "Placement office guide, section 1"),
    FAQ("Who should I contact about tuition payments?", "Contact the accounts office through the student portal. Include your student ID in your message; do not send full card details by email.", "Accounts office contact guide"),
]


def tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def retrieve(query: str) -> tuple[FAQ | None, float]:
    query_terms = tokens(query)
    scored = []
    for item in KNOWLEDGE_BASE:
        terms = tokens(item.question + " " + item.answer)
        overlap = len(query_terms & terms)
        score = overlap / max(1, len(query_terms))
        scored.append((score, item))
    score, item = max(scored, key=lambda pair: pair[0])
    return (item, score) if score >= 0.2 else (None, score)


def answer(query: str) -> str:
    item, score = retrieve(query)
    if item is None:
        return "I couldn't find a reliable answer in the campus guide. Please contact student services."
    return f"{item.answer}\n\nSource: {item.source} (match: {score:.0%})"


if __name__ == "__main__":
    print("Campus FAQ Agent — ask about the student portal, library, ID cards, internships, or payments. Type 'quit' to exit.")
    while True:
        question = input("\nYou: ").strip()
        if question.lower() in {"quit", "exit"}:
            break
        if question:
            print(f"\nAgent: {answer(question)}")

