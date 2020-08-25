def SQL_To_HTML_Table():
	
	Rows = ['Eins', 'Zwei', 'Drei', 'Vier']
	
	P1 = '<table>'
	PEnd = '</table>'
	String = P1
	
	String = String + '<tr>'
	
	
	for row in Rows:
	    String = String + '<td>'
	    String = String + row
	    String = String + '</td>' 
	String = String + PEnd 
	
	return String
	
if __name__ == '__main__':
	
	print SQL_To_HTML_Table()
	
