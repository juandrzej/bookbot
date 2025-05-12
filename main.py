from stats import count_words


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main() -> None:
    book_text: str = get_book_text("./books/frankenstein.txt")
    num_words: int = count_words(book_text)

    analysis_result: str = f"{num_words} words found in the document"
    print(analysis_result)


if __name__ == "__main__":
    main()
