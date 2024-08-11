import re


def extract_yt_term(command):
    pattern = r"play\s+(.*?)\s+on\s+youtube"
    match = re.search(pattern,command,re.IGNORECASE)
    return match.group(1) if match else None

def remove_words(input_string, words_to_remove):
    words = input_string.strip().split()
    print(words)
    filtered_words = [word for word in words if word.lower() not in words_to_remove]
    print(filtered_words)
    result_string = " ".join(filtered_words)
    print(result_string)
    return result_string