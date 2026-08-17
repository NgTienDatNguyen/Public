import json

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def analyze_market(data):
    print("--- 2026 GLOBAL MARKET TREND ANALYSIS ---")
    for item in sorted(data, key=lambda x: x['growth_rate_percent'], reverse=True):
        print(f"Domain: {item['domain']}")
        print(f"Growth Rate: {item['growth_rate_percent']}%")
        print(f"Entry Roles: {', '.join(item['entry_level_roles'])}")
        print("-" * 40)

if __name__ == "__main__":
    dataset = load_data('../data/tech_trends_2026.json')
    analyze_market(dataset)
