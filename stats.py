def count_words(text: str) -> int:
    """Function to count words in a given string. Returns integer."""
    return len(text.split())


def count_characters(text: str) -> dict[str, int]:
    """Function to count alphabetic characters in a given string. Returns dictionary with characters appearences."""
    chars_count: dict[str, int] = {}
    clean_text: str = "".join(char.lower() for char in text if char.isalpha())
    for char in clean_text:
        if char in chars_count:
            chars_count[char] += 1
        else:
            chars_count[char] = 1

    return chars_count


def restructure_character_count(
    input_dict: dict[str, int],
) -> list[dict[str, str | int]]:
    restructured_list: list[dict[str, str | int]] = []
    for key, value in input_dict.items():
        restructured_list.append({"char": key, "num": value})

    return sort_list(restructured_list)


def sort_on(input_dict: dict[str, str | int]) -> int:
    """Function that takes a dictionary and returns the value of the 'num' key"""
    return input_dict["num"]


def sort_list(input_list: list[dict[str, str | int]]) -> list[dict[str, str | int]]:
    """Function that sorts a list by 'num' key in each dictionary entry."""
    return sorted(input_list, reverse=True, key=sort_on)
