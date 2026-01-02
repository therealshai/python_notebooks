def cap_text(text):
    '''
    :param text: input String
    :return: Return capitalized text
    '''
    # capitalized_text = text.capitalize() -> first iteration
    capitalized_text = ''
    for char in text.split():
        capitalized_text = capitalized_text + " "+ char.capitalize()
    return capitalized_text.strip() #remove spaces from start& end of the string

# .title() function can also be used for this functionality