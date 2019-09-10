# Using indexed placeholders

markup = """
<!doctype html>
<html>
    <head>
        <title>{0}</title>
    </head>
    <body>
        <h1>{0}</h1>
    </body>
</html>
"""

markup = markup.format('My Page Title', 'My Page Heading')
print(markup)

# Using named placeholders

markup = """
<!doctype html>
<html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        <h1>{heading}</h1>
    </body>
</html>
"""

markup = markup.format(title='My Page Title', heading='My Page Heading')
print(markup)
