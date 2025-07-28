# ranker.py

def score_sections(sections, persona_json, job):
    for sec in sections:
        sec["score"] = 1.0  # Dummy static score
    return sections
