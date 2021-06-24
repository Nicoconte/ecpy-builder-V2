<h1> -- Easy Crud for Python - ecpy 🐍 -- </h1>

<h4> This is a little module to build queries for MySQL databases </h4>

<hr>

<p> You can find another version of this module made by me at https://github.com/Nicoconte/Easy-crud-for-python-ecpy </p>

<hr>

<h3> Example </h3>


```python
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

```