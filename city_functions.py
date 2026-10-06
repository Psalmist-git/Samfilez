def get_formatted_city(city, country, population=None):
    """Return a single string formatted with city, country, and optional population."""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    return f"{city.title()}, {country.title()}"
