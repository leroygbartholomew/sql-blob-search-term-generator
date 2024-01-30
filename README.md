# sql-blob-search-term-generator
Program to generate WHERE conditions for an SQLite query to then search BLOB data

# This program will take a search term and table.field name and process
# them to return lines that can be copied into a SQL or SQLite query
# to enable searching of BLOB fields for text strings.  If you're not
# sure about capitalization, it's better to capitalize the firs letter
# since the search will then be with the capital first letter and all
# letters both lower case.  
#
# Using -h or --help will provide the usage information.
