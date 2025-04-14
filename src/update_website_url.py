import sys
import os
# import fetch_rank

# Get the LeetCode username from the command line arguments
leetcode_username = sys.argv[1]

print("LeetCode username received:", leetcode_username)

script_dir = os.path.dirname(__file__)  # The directory where this script is located
fetch_rank_path = os.path.join(script_dir, "fetch_rank.py")  # If the script is inside src/

print("fetch_rank_path",fetch_rank_path)

# Read the content of fetch_rank.py
with open(fetch_rank_path, "r") as file:
    content = file.read()

# print("########## BEFORE #########")
# print("content content content content content",content)
# print("########### BEFORE ########")

# Replace the placeholder website URL with the user's LeetCode username
content = content.replace(
    "https://leetcode.com/u/username/", 
    f"https://leetcode.com/u/{leetcode_username}/"
)
# print("########## AFTER #########")
# print("content content content content content",content)
# print("########### AFTER ########")
# Write the updated content back to fetch_rank.py
with open(fetch_rank_path, "w") as file:
    file.write(content)

print(f"Updated fetch_rank.py with LeetCode username: {leetcode_username}")
