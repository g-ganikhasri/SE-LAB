
def sender_domain(email):
    if not isinstance(email, str):
        return ""

    if email.count('@') != 1:
        return ""

    local, domain = email.split('@')

    if not local or not domain:
        return ""

    return domain.lower()


def first_link(text):
    if not isinstance(text, str):
        return ""

    start = text.find('http')

    if start == -1:
        return ""

    end = text.find(' ', start)

    if end == -1:
        end = len(text)

    return text[start:end]


def shout_ratio(text):
    if not isinstance(text, str):
        return 0.0

    letters = [c for c in text if c.isalpha()]
    upper = [c for c in letters if c.isupper()]

    if len(letters) == 0:
        return 0.0

    return len(upper) / len(letters)


def main():
    print("==== Running sender_domain ====")
    user_input = input("Enter a sender email (e.g. offers@Deals.com): ")
    result = sender_domain(user_input)
    print("Sender Domain:", result)

    print("\n==== Running first_link ====")
    user_input = input("Enter a message containing a link: ")
    result = first_link(user_input)
    print("First Link:", result)

    print("\n==== Running shout_ratio ====")
    user_input = input("Enter a message (e.g. FREE prize NOW): ")
    result = shout_ratio(user_input)
    print("Uppercase Ratio:", result)


if __name__ == "__main__":
    main()
