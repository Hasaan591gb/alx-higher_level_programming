#include <Python.h>
#include <stdio.h>
#include <listobject.h>

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: Pointer to a Python object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, limit, i;
	char *str;
	PyBytesObject *object;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	object = (PyBytesObject *)p;
	size = object->ob_base.ob_size;
	str = object->ob_sval;
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	limit = size + 1;
	if (limit > 10)
		limit = 10;
	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
		printf(" %02x", str[i] & 0xff);
	printf("\n");
}


/**
 * print_python_list - Prints information about a Python list object
 * @p: Pointer to a Python object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyListObject *list = (PyListObject *)p;

	size = list->ob_base.ob_size;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, list->ob_item[i]->ob_type->tp_name);
		if (PyBytes_Check(list->ob_item[i]))
			print_python_bytes(list->ob_item[i]);
	}
}

