from builder.ecpy_builder import EcpyBuilder

def main():
	ecpy = EcpyBuilder({
		"host": "localhost", 
		"user": "root", 
		"password": "", 
		"db": "ecpy_test"
	})
	
	print(ecpy
		.insert()
		.table('user')
		.into(['id', 'username', 'password'])
		.bind([1, "root", "toor"])
		.exec()
	) # => True | False

if __name__ == "__main__":
    main()
