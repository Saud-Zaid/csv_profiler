def slugify(text: str ) -> str:
    """Turn 'Report Name' -> 'report-name' """
    return text.strip().lower().replace(" ", "-")


#print(__name__)
#print("before main")

#if __name__ == "__main__":
#    print(slugify("My Report 01"))
