def classify_error(error):

    error = error.lower()

    if "modulenotfounderror" in error:
        return "DEPENDENCY_ERROR"

    if "importerror" in error:
        return "IMPORT_ERROR"

    if "path" in error:
        return "ENVIRONMENT_ERROR"

    if "syntaxerror" in error:
        return "SYNTAX_ERROR"

    return "GENERAL_ERROR"