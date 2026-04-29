from utils.llm import call_llm

def analyze_code(code):
    prompt = f"""
Analyze the following Python code and identify:
1. Performance bottlenecks
2. Bad practices
3. Optimization opportunities

Code:
{code}
"""
    return call_llm(prompt)
