def main():
    # Prompt the user for a file name
    file_name = input("Enter a file name: ")

    # Get the media type based on the file name
    media_type = get_media_type(file_name)

    # Print the media type
    print(media_type)

def get_media_type(file_type):
    # Ignore leading and trailing whitespace and convert the file name to lowercase
    file_name = file_type.strip().lower()

    if file_name.endswith((".jpg", ".jpeg")):
        return "image/jpeg"
    elif file_name.endswith(".pdf"):
        return "application/pdf"
    elif file_name.endswith(".png"):
        return "image/png"
    elif file_name.endswith(".gif"):
        return "image/gif"
    elif file_name.endswith(".txt"):
        return "text/plain"
    elif file_name.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"

main()