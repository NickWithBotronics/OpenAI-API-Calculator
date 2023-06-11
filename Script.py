import argparse

def calculate_cost(version, tokens):
    cost_per_thousand = {
        'gpt3.5t': 0.002,
        'gpt4': 0.03
    }

    if version not in cost_per_thousand:
        print(f"Invalid version: {version}")
        return

    cost = (tokens / 1000) * cost_per_thousand[version]

    print(f"The cost for {tokens} tokens using {version} is ${cost:.2f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate API token costs.')
    parser.add_argument('version', type=str, help='The API version. Either "gpt3.5t" or "gpt4".')
    parser.add_argument('tokens', type=int, help='The number of tokens.')
    
    args = parser.parse_args()

    calculate_cost(args.version, args.tokens)
