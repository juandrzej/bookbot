def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main() -> None:
    book_text: str = get_book_text("./books/frankenstein.txt")
    print(book_text)


if __name__ == "__main__":
    main()
