# badge_generator.py

def generate_badge(label, message, color):
    """Generate a markdown badge using shields.io."""
    return f"![{label}](https://img.shields.io/badge/{label}-{message}-{color})"

def main():
    """Generate and print a list of common GitHub badges."""
    badges = {
        "GitHub Repo Size": generate_badge("Repo Size", "1MB", "blue"),
        "GitHub License": generate_badge("License", "MIT", "green"),
        "GitHub Stars": generate_badge("Stars", "100", "yellow"),
        "GitHub Forks": generate_badge("Forks", "50", "orange"),
        "GitHub Issues": generate_badge("Issues", "10", "red"),
        "GitHub Pull Requests": generate_badge("PRs", "5", "purple"),
        "GitHub Build": generate_badge("Build", "Passing", "brightgreen"),
        "Python Version": generate_badge("Python", "3.9", "blue"),
        "Contributions Welcome": generate_badge("Contributions", "Welcome", "brightgreen")
    }

    print("\n## GitHub Badges\n")
    for name, badge in badges.items():
        print(f"- **{name}**: {badge}")

if __name__ == "__main__":
    main()

