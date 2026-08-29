from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

TOPICS = {
    "01-Arrays": "Arrays",
    "02-Strings": "Strings",
    "03-Hashing": "Hashing",
    "04-Two-Pointers": "Two Pointers",
    "05-Sliding-Window": "Sliding Window",
    "06-Binary-Search": "Binary Search",
    "07-Linked-List": "Linked List",
    "08-Stack": "Stack",
    "09-Queue": "Queue",
    "10-Trees": "Trees",
    "11-Heap": "Heap",
    "12-Graphs": "Graphs",
    "13-Greedy": "Greedy",
    "14-Backtracking": "Backtracking",
    "15-Dynamic-Programming": "Dynamic Programming",
}


def get_solutions(folder):
    return sorted(folder.glob("*.py"), key=lambda file: file.name.lower())


def get_problem_title(file):
    return file.stem.replace("_", " ").title()


def get_difficulty(file):
    text = file.read_text(encoding="utf-8")

    match = re.search(
        r"Difficulty:\s*(Easy|Medium|Hard)",
        text,
        re.IGNORECASE
    )

    return match.group(1).capitalize() if match else "-"


def build_readme():
    total = 0
    topic_rows = []
    problem_rows = []

    for folder_name, topic_name in TOPICS.items():
        folder = ROOT / folder_name

        if folder.exists():
            solutions = get_solutions(folder)
        else:
            solutions = []

        total += len(solutions)

        topic_rows.append(
            f"| {topic_name} | {len(solutions)} |"
        )

        for solution in solutions:
            title = get_problem_title(solution)
            difficulty = get_difficulty(solution)

            problem_rows.append(
                f"| {title} | {topic_name} | {difficulty} |"
            )

    if not problem_rows:
        problem_rows.append("| No problems yet | - | - |")

    milestone_25 = "x" if total >= 25 else " "
    milestone_50 = "x" if total >= 50 else " "
    milestone_100 = "x" if total >= 100 else " "
    milestone_150 = "x" if total >= 150 else " "
    milestone_200 = "x" if total >= 200 else " "

    topic_table = "`n".join(topic_rows)
    problem_table = "`n".join(problem_rows)

    lines = [
        "# LeetCode DSA - Python",
        "",
        "A structured journey of solving Data Structures and Algorithms",
        "problems using Python.",
        "",
        "This repository contains my LeetCode solutions, approaches,",
        "examples, and complexity analysis.",
        "",
        "> One problem at a time. One concept at a time.",
        "",
        "---",
        "",
        "## Progress",
        "",
        f"**Total Problems Solved: {total}**",
        "",
        "| Topic | Problems Solved |",
        "|---|---:|",
        topic_table,
        "",
        "---",
        "",
        "## Problems Solved",
        "",
        "| Problem | Topic | Difficulty |",
        "|---|---|---|",
        problem_table,
        "",
        "---",
        "",
        "## Topics",
        "",
        "### Fundamentals",
        "",
        "- Arrays",
        "- Strings",
        "- Hashing",
        "- Two Pointers",
        "- Sliding Window",
        "- Binary Search",
        "",
        "### Data Structures",
        "",
        "- Linked List",
        "- Stack",
        "- Queue",
        "- Trees",
        "- Heap",
        "- Graphs",
        "",
        "### Algorithms",
        "",
        "- Greedy",
        "- Backtracking",
        "- Dynamic Programming",
        "",
        "---",
        "",
        "## Solution Format",
        "",
        "Each solution contains:",
        "",
        "- Problem name",
        "- LeetCode problem number",
        "- Difficulty",
        "- Approach",
        "- Python implementation",
        "- Example",
        "- Output",
        "- Time complexity",
        "- Space complexity",
        "",
        "---",
        "",
        "## Milestones",
        "",
        "- [x] Started DSA journey",
        "- [x] First LeetCode problem",
        f"- [{milestone_25}] 25 Problems",
        f"- [{milestone_50}] 50 Problems",
        f"- [{milestone_100}] 100 Problems",
        f"- [{milestone_150}] 150 Problems",
        f"- [{milestone_200}] 200 Problems",
        "",
        "---",
        "",
        "## Language",
        "",
        "**Python**",
        "",
        "All solutions in this repository are implemented in Python.",
        "",
        "---",
        "",
        "## Goals",
        "",
        "- Strengthen Data Structures and Algorithms",
        "- Improve Python problem-solving skills",
        "- Develop algorithmic thinking",
        "- Prepare for technical interviews",
        "- Maintain consistent coding practice",
        "",
        "---",
        "",
        "## Automatic Progress Tracking",
        "",
        "This README is generated automatically using Python.",
        "",
        "Whenever a new Python solution is added to a topic folder,",
        "the script automatically updates:",
        "",
        "- Total problems solved",
        "- Topic-wise problem count",
        "- Problem list",
        "- Difficulty",
        "- Milestones",
        "",
        "No manual README updates are required.",
        "",
        "---",
        "",
        "## Repository Structure",
        "",
        "```text",
        "LeetCode-DSA-Python/",
        "|-- 01-Arrays/",
        "|-- 02-Strings/",
        "|-- 03-Hashing/",
        "|-- 04-Two-Pointers/",
        "|-- 05-Sliding-Window/",
        "|-- 06-Binary-Search/",
        "|-- 07-Linked-List/",
        "|-- 08-Stack/",
        "|-- 09-Queue/",
        "|-- 10-Trees/",
        "|-- 11-Heap/",
        "|-- 12-Graphs/",
        "|-- 13-Greedy/",
        "|-- 14-Backtracking/",
        "|-- 15-Dynamic-Programming/",
        "|",
        "|-- scripts/",
        "|   |-- update_readme.py",
        "|",
        "|-- README.md",
        "```",
        "",
        "---",
        "",
        "## Learning Philosophy",
        "",
        "> Consistency over perfection.",
        "",
        "Keep learning.",
        "Keep solving.",
        "Keep improving.",
    ]

    README.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build_readme()
    print("README updated successfully!")
