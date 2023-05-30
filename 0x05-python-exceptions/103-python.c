#include <Python.h>
#include <stdio.h>
#include <listobject.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);


/**
 * print_python_float - prints information about a python float object
 * @p: pointer to a PyObject
 *
 * Return: void
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *object;

	printf("[.] float object info\n");
	fflush(stdout);
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		fflush(stdout);
		return;
	}

	object = (PyFloatObject *)p;
	printf("  value: %f\n", object->ob_fval);
	fflush(stdout);
}


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
	fflush(stdout);
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		fflush(stdout);
		return;
	}

	object = (PyBytesObject *)p;
	size = object->ob_base.ob_size;
	str = object->ob_sval;
	printf("  size: %ld\n", size);
	fflush(stdout);
	printf("  trying string: %s\n", str);
	fflush(stdout);

	limit = size + 1;
	if (limit > 10)
		limit = 10;
	printf("  first %ld bytes:", limit);
	fflush(stdout);

	for (i = 0; i < limit; i++)
		printf(" %02x", str[i] & 0xff);
	printf("\n");
	fflush(stdout);
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
	fflush(stdout);
	printf("[*] Size of the Python List = %ld\n", size);
	fflush(stdout);
	printf("[*] Allocated = %ld\n", list->allocated);
	fflush(stdout);

	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, list->ob_item[i]->ob_type->tp_name);
		fflush(stdout);
		if (PyBytes_Check(list->ob_item[i]))
			print_python_bytes(list->ob_item[i]);
		else if (PyFloat_Check(list->ob_item[i]))
			print_python_float(list->ob_item[i]);
	}
}
