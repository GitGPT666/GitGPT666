from agents.analyzer import analyze_code
from agents.optimizer import generate_optimization
from agents.executor import save_code

def main():
    code = """
def slow_function():
    result = []
    for i in range(10000):
        for j in range(10000):
            result.append(i * j)
    return result
"""

    print("🚀 Step 1: 分析代码...")
    analysis = analyze_code(code)
    print(analysis)

    print("\n⚡ Step 2: 生成优化方案...")
    optimized_code = generate_optimization(code, analysis)
    print(optimized_code)

    print("\n💾 Step 3: 保存优化代码...")
    file = save_code(optimized_code)

    print(f"\n✅ 优化完成，文件保存为: {file}")

if __name__ == "__main__":
    main()
