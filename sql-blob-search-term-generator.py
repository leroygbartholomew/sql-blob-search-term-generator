# SQL-BLOB SEARCH TERM GENERATOR
# Version 1.0
# Date  2024-01-29
# Copyright (C) 2024 - Aaron Dee Roberts
#
# This program will take a search term and table.field name and process
# them to return lines that can be copied into a SQL or SQLite query
# to enable searching of BLOB fields for text strings.  If you're not
# sure about capitalization, it's better to capitalize the firs letter
# since the search will then be with the capital first letter and all
# letters both lower case.  
#
# Using -h or --help will provide the usage information.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You can view the GNU General Public License at <http://www.gnu.org/licenses/>


import sys

# PRE DEFINE VARIABLES

i_count = 0 # Set variables
l_letters = [] # Set variables
l_hexletters = []
l_hexlettersuc = []
s_temp = ''
h_temp = ''
s_search = ''
s_table = ''
l_letters_lc = []
l_hexletters_lc = []
l_hexlettersuc_lc = []
l_letters_uc = []
l_hexletters_uc = []
l_hexlettersuc_uc = []

#print()
#print ('argument list', sys.argv)


# MAKE SURE THERE ARE NO INDEX ERRORS AND TELL WHY IF THERE IS
try:
	s_message_err = """
You need to specify the correct arguments.

Format: Command.py [search item] [table.field]
    Example: program.py "item to search for" table_to_look_in.field_to_search
    
	"""
	
	s_message_h = """
This program will take two arguments and make the "WHERE" portion of a
SQLite query to search BLOB data for text strings.  It will formrat the
output to search for the text as typed (capitals in certain places), 
all capitals, all lower case, and their unicode variants.  You can then
copy the output and insert it into your query.  If your search term
includes spaces, make sure to put it in double quotes.

Format: Command.py [search item] [table.field]
    Example: program.py "item to search for" table_to_look_in.field_to_search
    
	"""
	
	if sys.argv[1] == '-h' or sys.argv[1] == '--help':
		print(s_message_h)
		quit()
		
	s_search = sys.argv[1]
	s_search_lc = sys.argv[1].lower()
	s_search_uc = sys.argv[1].upper()
	s_table = sys.argv[2]
except IndexError:
	print(s_message_err)
	quit()

def parse_hex(s_search, s_table):
	i_len = len(s_search)

	i_count = 0
	
	# CONVERT AS TYPED
	while i_count < i_len:
		i_count +=1
		s_temp = s_search[i_count - 1:i_count]
		s_htemp = str(hex(ord(s_temp))[2:]).upper() # "ord" retrieves the hex for the ascii character
		l_letters.append(s_temp) # Add the ASCII letters to a list
		l_hexletters.append(s_htemp) # Add the HEX byte to a list
		s_htemp = s_htemp + '00' # Add a 00 for the unicode portion
		l_hexlettersuc.append(s_htemp) # Add those now unicode bytes to a list. 
	
	s_search_hex_ascii = ''.join(l_hexletters) # Make the list into a string
	s_search_hex_uc = ''.join(l_hexlettersuc) # Make the list into a string
	
	i_count = 0
	
	# CONVERT LOWER CASE
	while i_count < i_len:
		i_count +=1
		s_temp = s_search_lc[i_count - 1:i_count]
		s_htemp = str(hex(ord(s_temp))[2:]).upper() # "ord" retrieves the hex for the ascii character
		l_letters_lc.append(s_temp) # Add the ASCII letters to a list
		l_hexletters_lc.append(s_htemp) # Add the HEX byte to a list
		s_htemp = s_htemp + '00' # Add a 00 for the unicode portion
		l_hexlettersuc_lc.append(s_htemp) # Add those now unicode bytes to a list. 
	
	s_search_hex_ascii_lc = ''.join(l_hexletters_lc) # Make the list into a string
	s_search_hex_uc_lc = ''.join(l_hexlettersuc_lc) # Make the list into a string
	
	i_count = 0
	# CONVERT UPPER CASE
	while i_count < i_len:
		i_count +=1
		s_temp = s_search_uc[i_count - 1:i_count]
		s_htemp = str(hex(ord(s_temp))[2:]).upper() # "ord" retrieves the hex for the ascii character
		l_letters_uc.append(s_temp) # Add the ASCII letters to a list
		l_hexletters_uc.append(s_htemp) # Add the HEX byte to a list
		s_htemp = s_htemp + '00' # Add a 00 for the unicode portion
		l_hexlettersuc_uc.append(s_htemp) # Add those now unicode bytes to a list. 
	
	s_search_hex_ascii_uc = ''.join(l_hexletters_uc) # Make the list into a string
	s_search_hex_uc_uc = ''.join(l_hexlettersuc_uc) # Make the list into a string
	
	
	#print(s_search)
	#print(s_search_hex_ascii)
	#print(s_search_hex_uc)
	#print(s_search_lc)
	#print(s_search_hex_ascii_lc)
	#print(s_search_hex_uc_lc)
	#print(s_search_uc)
	#print(s_search_hex_ascii_uc)
	#print(s_search_hex_uc_uc)
	
	s_query_part = f"""
--AS TYPED "{s_search}"
WHERE HEX({s_table}) LIKE "%{s_search_hex_ascii}%" 
OR HEX({s_table}) LIKE "%{s_search_hex_uc}%" 
-- LOWER CASE "{s_search_lc}"
OR HEX({s_table}) LIKE "%{s_search_hex_ascii_lc}%" 
OR HEX({s_table}) LIKE "%{s_search_hex_uc_lc}%" 
-- UPPER CASE "{s_search_uc}"
OR HEX({s_table}) LIKE "%{s_search_hex_ascii_uc}%" 
OR HEX({s_table}) LIKE "%{s_search_hex_uc_uc}%" 
"""
	print(s_query_part)
	
parse_hex(s_search, s_table)

