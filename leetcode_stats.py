import time, requests

LEETCODE_USERNAME = 'ranadeep_mahendra2426'

def fetch():
    resp = requests.get(f'https://leetcode-stats-api.herokuapp.com/{LEETCODE_USERNAME}')
    resp.raise_for_status()
    return resp.json()

def write(data):
    ts = int(time.time())
    with open('README.md', 'w') as f:
        f.write("# 👋 Hi, I'm Ranadeep Mahendra!\n\n")
        f.write("## 🏆 My LeetCode Progress\n\n")
        for label,color,solved,total in [
            ("Solved","blue", data['totalSolved'],  data['totalQuestions']),
            ("Easy",  "brightgreen", data['easySolved'],  data['totalEasy']),
            ("Medium","orange",     data['mediumSolved'],data['totalMedium']),
            ("Hard",  "red",        data['hardSolved'],  data['totalHard'])
        ]:
            f.write(
                f"![{label}]"
                f"(https://img.shields.io/badge/{label}-{solved}/{total}-{color}?cache={ts}) "
            )
        f.write("\n\n### 📊 LeetCode Activity Graph\n\n")
        f.write(
            f"![Heatmap]"
            f"(https://leetcard.jacoblin.cool/{LEETCODE_USERNAME}?theme=dark&font=Karma&ext=heatmap&cache={ts})\n"
        )

if __name__ == "__main__":
    write(fetch())
