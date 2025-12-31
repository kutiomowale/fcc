def create_spend_chart(categories):
    spent = [cat.total_withdrawals() for cat in categories]
    total = sum(spent)

    # round DOWN to nearest 10
    percentages = [(int((s / total) * 100) // 10) * 10 for s in spent]

    lines = []
    lines.append("Percentage spent by category")

    # bars
    for level in range(100, -1, -10):
        line = f"{level:>3}| "
        for p in percentages:
            line += "o  " if p >= level else "   "
        lines.append(line)

    # horizontal line (exact length)
    lines.append("    " + "---" * len(categories) + "-")

    # vertical category names
    names = [cat.name for cat in categories]
    max_len = max(len(name) for name in names)

    for i in range(max_len):
        line = "     "
        for name in names:
            if i < len(name):
                line += name[i] + "  "
            else:
                line += "   "
        lines.append(line)

    return "\n".join(lines)
