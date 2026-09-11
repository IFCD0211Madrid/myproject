def run(text: str) -> bool:
    # TODO
    isogram = True
    text = text.lower()
    for i in range(len(text)):
        if text[i].isalpha() \
        and (text[i] in text[:i] \
             or text[i] in text[i+1:]):
            isogram = False
            break
    return isogram


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
