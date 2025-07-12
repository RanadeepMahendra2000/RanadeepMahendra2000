import time
import requests

LEETCODE_USERNAME = 'ranadeep_mahendra2426'  # Replace with your actual LeetCode username

def fetch_leetcode_data(username):
    url = f'https://leetcode-stats-api.herokuapp.com/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data:", response.status_code)
        return None

def update_readme(data):
    ts = int(time.time())  # cache‐buster timestamp
    with open('README.md', 'w') as f:
        f.write("# 👋 Hi, I'm Ranadeep Mahendra!\n\n")
        f.write("## 🏆 My LeetCode Progress\n\n")
        f.write(f"![LeetCode Questions Solved]"
                f"(https://img.shields.io/badge/Solved-{data['totalSolved']}/{data['totalQuestions']}-blue)\n")
        f.write(f"![LeetCode Easy]"
                f"(https://img.shields.io/badge/Easy-{data['easySolved']}/{data['totalEasy']}-brightgreen)\n")
        f.write(f"![LeetCode Medium]"
                f"(https://img.shields.io/badge/Medium-{data['mediumSolved']}/{data['totalMedium']}-orange)\n")
        f.write(f"![LeetCode Hard]"
                f"(https://img.shields.io/badge/Hard-{data['hardSolved']}/{data['totalHard']}-red)\n\n")
        f.write("### 📊 LeetCode Activity Graph\n\n")
        f.write(
            f"![LeetCode Activity Graph]"
            f"(https://leetcard.jacoblin.cool/{LEETCODE_USERNAME}"
            f"?theme=dark&font=Karma&ext=heatmap&cache={ts})\n"
        )

if __name__ == "__main__":
    data = fetch_leetcode_data(LEETCODE_USERNAME)
    if data:
        update_readme(data)
