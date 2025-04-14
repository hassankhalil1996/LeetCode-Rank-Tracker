import sys

# Get the LeetCode username from the command line arguments
leetcode_username = sys.argv[1]

# Read the content of fetch_rank.py
with open("fetch_rank.py", "r") as file:
    content = file.read()

# Replace the placeholder website URL with the user's LeetCode username
content = content.replace('website = \'https://leetcode.com/u/username/\'', f'website = \'https://leetcode.com/u/{leetcode_username}/\'')

# Write the updated content back to fetch_rank.py
with open("fetch_rank.py", "w") as file:
    file.write(content)

print(f"Updated fetch_rank.py with LeetCode username: {leetcode_username}")
