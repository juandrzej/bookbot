import sys
from stats import count_words, count_characters, restructure_character_count


def get_book_text(filepath: str) -> str:
    """Function to extract a string from a text file."""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main() -> None:
    # Main program workflow
    try:
        path: str = sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text: str = get_book_text(path)
    num_words: int = count_words(book_text)
    num_chars: dict[str, int] = count_characters(book_text)
    clean_list: list[dict[str, str | int]] = restructure_character_count(num_chars)

    # Create the analysis result string
    analysis_result: str = (
        "============ BOOKBOT ============\n"
        f"Analyzing book found at {path}...\n"
        "----------- Word Count ----------\n"
        f"Found {num_words} total words\n"
        "--------- Character Count -------\n"
    )

    # Add each character count to the output
    for entry in clean_list:
        analysis_result += f"{entry['char']}: {entry['num']} \n"

    # Add the footer
    analysis_result += "============= END ==============="

    print(analysis_result)


if __name__ == "__main__":
    main()
