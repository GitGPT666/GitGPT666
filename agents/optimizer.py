from utils.llm import call_llm

def generate_optimization(code, analysis):
    prompt = f"""
Based on the analysis below, generate an optimized version of the code.

Analysis:
{analysis}

Original Code:
{code}

Output only improved code.
"""
    return call_llm(prompt)
